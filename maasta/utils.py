# MAASTA (MAAS Terraform Ansible)
# Copyright 2021 Saeid Bostandoust <ssbostan@linuxmail.org>

from json import dumps, loads
from yaml import dump
import configparser


class NestedDict(dict):

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


class AnsibleInventory:

    def __init__(self):
        self.inventory = NestedDict()
        self.ini_inventory = NestedDict()
        self.config = configparser.ConfigParser(delimiters=' ')

    def add(self, group, machine):
        self.inventory["all"]["hosts"][machine.fqdn]["ansible_host"] = machine.ip_addresses[0]
        self.inventory["all"]["hosts"][machine.fqdn]["ansible_user"] = "ubuntu"
        self.inventory["all"]["hosts"][machine.fqdn]["machine_id"] = machine.system_id
        self.inventory["all"]["hosts"][machine.fqdn]["machine_hostname"] = machine.hostname
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn]["ansible_host"] = machine.ip_addresses[0]
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn]["ansible_user"] = "ubuntu"
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn]["machine_id"] = machine.system_id
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn]["machine_hostname"] = machine.hostname

    def dump(self):
        return dump(loads(dumps(self.inventory)))

    def dump_ini(self):
        for section in self.inventory["all"]["children"]:
            if not self.config.has_section(section):
                self.config.add_section(section)
            for val in self.inventory["all"]["children"][section]["hosts"]:
                self.config[section][val] = f'ansible_user={self.inventory["all"]["children"][section]["hosts"][val]["ansible_user"]}\
                        ansible_host={self.inventory["all"]["children"][section]["hosts"][val]["ansible_host"]}'
        return self.config

