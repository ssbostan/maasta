# MAASTA Examples

Three MAASTA examples are demonstrated in this directory:

 - **single**: A single machine that is provisioned by the Terraform and then the Docker will be installed by Ansible on it.
 - **count**: Multiple machines are provisioned by Terraform with a **count** meta-argument.
 - **multi**: Multiple resources and multiple machines are provisioned by the Terraform with a **count** meta-argument.

## How Terraform resources are converted to Ansible inventory:

All Terraform **maas_instance** resources will be grouped into the **[all]** of the Ansible inventory. Moreover, each **maas_instance** resource will be caused to create a new group in the Ansible inventory. The group name is the name of Terraform resource, and group members are instances of that resource. When multiple instances are provisioned in the same Terraform resource (by using **count** meta-argument), all of them are grouped into the same group in the Ansible inventory. Inventory is saved into **inventory.yaml** in YAML syntax.

## How to start:

To start using MAASTA install prerequisites.

 1. MAAS 2.9+
 2. Terraform 1.0+
 3. Ansible 2.7+

```bash
apt install -y python3-pip python3-venv

python -m venv venv

source venv/bin/activate

pip install -U pip

git clone https://github.com/ssbostan/maasta

cd maasta

pip install .

cd examples/single

export MAAS_API_URL=http://YOUR-MAAS-API-URL:5240/MAAS
export MAAS_API_KEY=YOUR-MAAS-API-KEY

./deploy
```
