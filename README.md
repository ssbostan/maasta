# MAASTA (MAAS Terraform Ansible)

MAASTA is a wrapper to create an Ansible inventory for MAAS instances that are provisioned by Terraform.

This script is used to build an end to end automation DevOps lifecycle.

## What is MAAS?

MAAS (Metal as a Service) is a tool to turns real servers into bare-metal cloud. With MAAS, you can automate server provisioning and installing OS remotely on both physical and virtual servers. [MAAS.io](https://maas.io/) for more information.

## What is Terraform?

Terraform is an infrastructure as code tool which is used originally for provisioning cloud instances on various cloud providers. With Terraform and the aid of the IaC, we can provision machines and cloud instances with codes and without direct human interactions. Terraform is responsible for provisioning systems, usually Immutable ones. [Terraform.io](https://www.terraform.io/) for more information.

## What is Ansible?

Ansible is another IaC tool but for configuration management. With the aid of Ansible, we can configure a multitude of systems without direct human interactions. Ansible is responsible for configuring existing systems, usually mutable ones. [Ansible.com](https:/ansible.com/) for more information.

# Why do we need MAASTA?

Imagine you want to create the DevOps lifecycle for your on-premises infrastructure. In such a scenario, You need the MAAS to interact with your real infrastructure and bring your bare-metal or virtual machines into cloud-like infrastructure. After that, to achieve automation, you need the Terraform tool to interact with the MAAS to provisioning instances and managing them without direct human interactions. When the instances, machines, were provisioned by the Terraform, the time to configuring them comes. For configuring instances, you need the Ansible tool, but how Ansible can discover targets that are provisioned by the Terraform. The answer is MAASTA! MAASTA is used to discover Terraform provisioned MAAS instances and create an Ansible inventory file for them. With the aid of the MAASTA, you can create an end to end automation and integrate MAAS, Terraform, and Ansible together.

See [/examples/README.md](https://github.com/ssbostan/maasta/tree/master/examples) to get started with brief examples.

# Get started guide:

MAASTA accepts two environment variables, **MAAS_API_URL** and **MAAS_API_KEY**, and reads the output of the **terraform show -json** command from **stdin**. The output of the Terraform is used to find the MAAS machines that are provisioned by the Terraform. MAASTA connects to the MAAS server and reads information (fqdn, hostname, ipaddr) of machines and creates an Ansible inventory for them. The inventory will write into **inventory.yaml** file.

### Installation:

```bash
pip install git+https://github.com/ssbostan/maasta.git
```

### Usage:

```bash
terraform show -json | python -m maasta
```

# How to contribute:

Currently, MAASTA can create inventory for machines that are provisioned with Ubuntu distribution. The script is tested with minimum viable tests and may break in some situations. Don't hesitate to contribute. In the case of a bug, please file an issue.

Copyright 2021 Saeid Bostandoust <ssbostan@linuxmail.org>
