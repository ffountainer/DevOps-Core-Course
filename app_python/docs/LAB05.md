# Documentation

## Architecture Overview

### Ansible version used

core 2.20.2

### Target VM OS and version

linux, ubuntu-2204-lts

### Role structure diagram or explanation

### Why roles instead of monolithic playbooks?

## Roles Documentation

first run

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/provision.yml

PLAY [Provision web servers] *********************************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************************
ok: [terraform]

TASK [common : Update apt cache] *****************************************************************************************************************************************************
changed: [terraform]

TASK [common : Install common packages] **********************************************************************************************************************************************
changed: [terraform]

TASK [common : Ensure timezone is set] ***********************************************************************************************************************************************
changed: [terraform]

TASK [docker : Install prerequisites] ************************************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker GPG key] ***************************************************************************************************************************************************
changed: [terraform]

TASK [docker : Add Docker APT repository] ********************************************************************************************************************************************
[WARNING]: Deprecation warnings can be disabled by setting `deprecation_warnings=False` in ansible.cfg.
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/docker/defaults/main.yml:7:14

5 docker_user: "ubuntu"
6 docker_gpg_url: "https://download.docker.com/linux/ubuntu/gpg"
7 docker_repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
               ^ column 14

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

changed: [terraform]

TASK [docker : Install Docker packages] **********************************************************************************************************************************************
changed: [terraform]

TASK [docker : Ensure Docker service is running] *************************************************************************************************************************************
ok: [terraform]

TASK [docker : Add user to Docker group] *********************************************************************************************************************************************
changed: [terraform]

TASK [docker : Install python3-docker for Ansible Docker modules] ********************************************************************************************************************
changed: [terraform]

RUNNING HANDLER [docker : restart docker] ********************************************************************************************************************************************
changed: [terraform]

PLAY RECAP ***************************************************************************************************************************************************************************
terraform                  : ok=12   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(devops) fountainer@Veronicas-MacBook-Air ansible % 
```

second run 

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/provision.yml

PLAY [Provision web servers] *********************************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************************
ok: [terraform]

TASK [common : Update apt cache] *****************************************************************************************************************************************************
ok: [terraform]

TASK [common : Install common packages] **********************************************************************************************************************************************
ok: [terraform]

TASK [common : Ensure timezone is set] ***********************************************************************************************************************************************
ok: [terraform]

TASK [docker : Install prerequisites] ************************************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker GPG key] ***************************************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker APT repository] ********************************************************************************************************************************************
[WARNING]: Deprecation warnings can be disabled by setting `deprecation_warnings=False` in ansible.cfg.
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/docker/defaults/main.yml:7:14

5 docker_user: "ubuntu"
6 docker_gpg_url: "https://download.docker.com/linux/ubuntu/gpg"
7 docker_repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
               ^ column 14

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

ok: [terraform]

TASK [docker : Install Docker packages] **********************************************************************************************************************************************
ok: [terraform]

TASK [docker : Ensure Docker service is running] *************************************************************************************************************************************
ok: [terraform]

TASK [docker : Add user to Docker group] *********************************************************************************************************************************************
ok: [terraform]

TASK [docker : Install python3-docker for Ansible Docker modules] ********************************************************************************************************************
ok: [terraform]

PLAY RECAP ***************************************************************************************************************************************************************************
terraform                  : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(devops) fountainer@Veronicas-MacBook-Air ansible % 
```

## Idempotency Demonstration

## Ansible Vault Usage

## Deployment Verification

## Key Decisions

## Challenges