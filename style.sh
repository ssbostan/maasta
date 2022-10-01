#!/usr/bin/bash

# MAASTA (MAAS Terraform Ansible)
# https://github.com/ssbostan/maasta

isort --py 310 maasta setup.py
black -t py310 maasta setup.py
