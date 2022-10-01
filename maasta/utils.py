# MAASTA (MAAS Terraform Ansible)
# https://github.com/ssbostan/maasta

from json import dumps, loads

from yaml import dump


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

    def add(self, group, machine):
        self.inventory["all"]["hosts"][machine.fqdn][
            "ansible_host"
        ] = machine.ip_addresses[0]
        self.inventory["all"]["hosts"][machine.fqdn]["ansible_user"] = "ubuntu"
        self.inventory["all"]["hosts"][machine.fqdn]["machine_id"] = machine.system_id
        self.inventory["all"]["hosts"][machine.fqdn][
            "machine_hostname"
        ] = machine.hostname
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn][
            "ansible_host"
        ] = machine.ip_addresses[0]
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn][
            "ansible_user"
        ] = "ubuntu"
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn][
            "machine_id"
        ] = machine.system_id
        self.inventory["all"]["children"][group]["hosts"][machine.fqdn][
            "machine_hostname"
        ] = machine.hostname

    def dump(self):
        return dump(loads(dumps(self.inventory)))
