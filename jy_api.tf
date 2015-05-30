variable "app_path" {
  default = "/var/www/jy_api/"
}

# Create a new Web droplet in the nyc2 region
resource "digitalocean_droplet" "jy_api" {
    image = "docker"
    name = "jy-api-1"
    region = "nyc3"
    size = "512mb"
    ssh_keys = [
      "${var.ssh_fingerprint}"
    ]

    connection {
      user = "root"
      type = "ssh"
      key_file = "${var.pvt_key}"
      timeout = "2m"
    }

    # create our remote directory
    provisioner "remote-exec" {
      inline = [
        "mkdir -p ${var.app_path}"
      ]
    }

    # copy our files...
    provisioner "file" {
        source = "./api"
        destination = "${var.app_path}"
    }
    provisioner "file" {
        source = "./nginx"
        destination = "${var.app_path}"
    }
    provisioner "file" {
        source = ".env"
        destination = "${var.app_path}.env"
    }
    provisioner "file" {
        source = "production.yml"
        destination = "${var.app_path}production.yml"
    }

    provisioner "remote-exec" {
      inline = [
        "export PATH=$PATH:/usr/bin",
        # install docker-compose,
        "sudo apt-get update",
        "sudo apt-get -y install python-pip",
        "sudo pip install -U docker-compose",
        # set up our docker containers,
        "cd ${var.app_path}",
        "docker-compose -f production.yml build",
        "docker-compose -f production.yml up -d",
        # set up db,
        "docker-compose -f production.yml run api /usr/local/bin/python manage.py migrate"
      ]
    }
}

# Create a new domain record
resource "digitalocean_domain" "default" {
    name = "api.jonryoung.com"
    ip_address = "${digitalocean_droplet.jy_api.ipv4_address}"
}
