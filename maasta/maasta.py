# MAASTA (MAAS Terraform Ansible)
# Copyright 2021 Saeid Bostandoust <ssbostan@linuxmail.org>

from json import loads
from sys import exit, stdin
from os import environ

from maas.client import connect
from maas.client.utils.creds import Credentials
from validators import url

from maasta.utils import AnsibleInventory

MAAS_API_URL = environ.get("MAAS_API_URL", None)
MAAS_API_KEY = environ.get("MAAS_API_KEY", None)

def main():

    if MAAS_API_URL is None:
        print("ERROR: Set MAAS_API_URL environment variable.")
        exit(1)

    if MAAS_API_KEY is None:
        print("ERROR: Set MAAS_API_KEY environment variable.")
        exit(1)

    if not url(MAAS_API_URL):
        print("ERROR: Invalid MAAS API url address.")
        exit(1)

    try:
        Credentials.parse(MAAS_API_KEY) # Validate X:Y:Z token format.
    except:
        print("ERROR: Invalid MAAS API key.")
        exit(1)

    input_data = stdin.read().strip() # Input JSON data from stdin.

    if not input_data:
        print("ERROR: Invalid input data.")
        exit(1)

    try:
        json_data = loads(input_data) # Convert JSON string to python dictionary.
    except:
        print("ERROR: Invalid JSON data.")
        exit(1)

    try:
        maas_client = connect(MAAS_API_URL, apikey=MAAS_API_KEY) # Connect to MAAS server.
    except:
        print("ERROR: Cannot connect to MAAS server.")
        exit(1)

    inventory = AnsibleInventory()

    for resource in json_data["values"]["root_module"]["resources"]:
        if resource["type"] == "maas_instance":
            try:
                machine = maas_client.machines.get(system_id=resource["values"]["id"])
            except:
                print("ERROR: Cannot get MAAS instance info.")
                exit(1)
            inventory.add(resource["name"], machine) # Adding machine into ansible inventory.

    try:
        with open("inventory.yaml", "w") as f:
            f.write(inventory.dump())
    except:
        print("ERROR: Cannot create inventory.yaml file.")
        exit(1)
    else:
        print("INFO: Ansible inventory created successfully.")
