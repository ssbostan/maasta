terraform {
  required_providers {
    maas = {
      source = "suchpuppet/maas"
      version = "~> 3.1.3"
    }
  }
}

variable "MAAS_API_KEY" {
  type = string
}

variable "MAAS_API_URL" {
  type = string
  default = "http://192.168.10.2:5240/MAAS"
}

provider "maas" {
  api_version = "2.0"
  api_key = var.MAAS_API_KEY
  api_url = var.MAAS_API_URL
}

resource "maas_instance" "webservers" {
  count = 3
  release_erase = false
  release_erase_quick = true
}

resource "maas_instance" "loadbalancers" {
  count = 2
  release_erase = false
  release_erase_quick = true
}
