variable "cf_token" {}
variable "cf_email" {}
variable "cf_domain" {}


provider "cloudflare" {
  email = "${var.cf_email}"
  token = "${var.cf_token}"
}
