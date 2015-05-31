## The Jon Young API

This project builds a [Django] (https://www.djangoproject.com/) App that serves an API that describes various roles I hold (or would like to hold), as well as tasks and interests associated with those roles. 

The project is built using [Django-REST-Framework] (http://www.django-rest-framework.org/), which provides a human browsable UI at `/`. Additionally I've enabled a [Swagger UI] (http://swagger.io/) integration at `/interactive/` for interactively exploring the API.

## Installing

Clone this repo:
```
git clone https://github.com/thejaywhy/roles_api
```

### virtualenv

If you're into using virtual environments:

```
virtualenv venv
source venv/bin/activate
cd api
pip install -r requirements.txt
python manage.py runserver
```
Now visit http://localhost:8000 or http://localhost:8000/interactive/ in your web browser.

### Docker
This repo also ships with support for Docker-Compose and Docker-Machine for local development. Follow these commands to spin up the API service:

```
docker-machine create -d virtualbox dev;
eval "$(docker-machine env dev)"
docker-compose build
docker-compose up -d
docker-machine ip dev
```
Now you can go visit that IP address in a web browser! Don't forget to append `/interactive/` to check out the Swagger UI powered docs.

## Running Tests
To run the included tests, you'll need to install the [requests] (http://docs.python-requests.org/en/latest/#) library. I used `requests` instead of the Django Test Client because allows for more of a high level functional test (in my opinion at least).

```
pip install -r test-requirements.txt
python manage.py test
```

## Deploying
You should start by cloning this repo locally.

You'll want to modify the `.env` file to have values that make sense for your deployment whether using Terraform or Docker-Machine.

Also, I've included Django database migrations that will populate the data store with data that pertains to me. So if you don't want that, you may want to remove some of them from `/api/jy_api/apps/api/migrations`.

### Terraform
The deployment that I'm favoring uses [Terraform] (https://terraform.io/) to spin up a Digital Ocean droplet with docker installed. It then copies files from this repo, and installs docker-compose. Once everything is installed, docker-compose is used to spin up NGINX, PostgreSQL, and an application container.

Finally Terraform will create a DNS entry for [CloudFlare] (https://www.cloudflare.com/) that points to the DO Droplet.

I'm not excited about the way I've chosen to install dependencies on the droplet, but it does work, and that's the best part!

Here's all you have to do to spin everything up:

```bash
export TF_VAR_do_token={your_PAT}
export TF_VAR_ssh_fingerprint=$(ssh-keygen -lf ~/.ssh/id_rsa.pub | awk '{print $2}')
export TF_VAR_pub_key=$HOME/.ssh/id_rsa.pub
export TF_VAR_pvt_key=$HOME/.ssh/id_rsa
export TF_VAR_cf_token={your_token}
export TF_VAR_cf_email={your_email}
export TF_VAR_cf_domain={your_domain}
export TF_VAR_cf_subdomain={your_subdomain}
terraform plan
# Hit 'enter' to accept default remote path to install too
# terraform plan will show you what's going to happen before you actually do anything.
terraform apply
```
While all that spins up, you'll probably want to do something else for a while. Now is your chance to read that book you've been meaning to get to.

When `terraform` completes, you should be able to go check out the site (assuming minimal DNS propagation times).

### Docker-Machine
You can also use the fancy new [docker-machine] (http://docs.docker.com/machine/) to spin up a Digital Ocean droplet, but you won't get the DNS integration. Here's what you need to make it happen:

```bash
docker-machine create \
-d digitalocean \
--digitalocean-access-token=${your_PAT} \
production
docker-machine active production
eval "$(docker-machine env production)"
docker-compose build
docker-compose up -d -f production.yml
docker-compose run web /usr/local/bin/python manage.py migrate
docker-machine ip production
```

Now you can visit your droplet's IP address to see the API out in the wild.

## Acknowledgments

The Docker stuff comes from this awesome RealPython Blog post -> https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/

## TODO
1. Get Navbar links from the Link models directly.
2. Look at making different YAML files for docker-compose to consume.
3. Use template for NGINX config (server_name, port).
4. Clean up / Simplify Terraform provisioners.

## Author
[thejaywhy] (https://github.com/thejaywhy)
