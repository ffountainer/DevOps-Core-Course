# Documentation

## Overview (What you accomplished and technologies used)

## Blocks & Tags (Block usage in each role, tag strategy, execution examples with screenshots)

### Test provision with only docker
![](./screenshots/lab06-shots/Test%20provision%20with%20only%20docker.png)

### Skip common role
![](./screenshots/lab06-shots/Skip%20common%20role.png)

### Install packages only across all roles
![](./screenshots/lab06-shots/Install%20packages%20only%20across%20all%20roles.png)

### Check mode to see what would run
![](./screenshots/lab06-shots/Check%20mode%20to%20see%20what%20would%20run.png)

### Run only docker installation tasks
![](./screenshots/lab06-shots/Run%20only%20docker%20installation%20tasks.png)

### Error handling with rescue block triggered

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/provision.yml --tags "docker_install"

PLAY [Provision web servers] ********************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************
ok: [terraform]

TASK [docker : Install prerequisites] ***********************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker GPG key] **************************************************************************************************************************************
[ERROR]: Task failed: Module failed: unknown url type: 'blabla'
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/docker/tasks/main.yml:14:7

12         state: present
13         update_cache: yes
14     - name: Add Docker GPG key
         ^ column 7

fatal: [terraform]: FAILED! => {"changed": false, "msg": "unknown url type: 'blabla'", "status": -1, "url": "blabla"}

TASK [docker : Wait before retry] ***************************************************************************************************************************************
Pausing for 10 seconds
(ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
ok: [terraform]

TASK [docker : Retry apt update] ****************************************************************************************************************************************
changed: [terraform]

TASK [docker : Retry adding Docker GPG key] *****************************************************************************************************************************
ok: [terraform]

TASK [docker : ensure docker service is enabled] ************************************************************************************************************************
ok: [terraform]

PLAY RECAP **************************************************************************************************************************************************************
terraform                  : ok=6    changed=1    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
```

### List all available tags

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/provision.yml --list-tags

playbook: playbooks/provision.yml

  play #1 (webservers): Provision web servers   TAGS: []
      TASK TAGS: [common, docker, docker_config, docker_install, packages, timezone, users]
```

## Docker Compose Migration (Template structure, role dependencies, before/after comparison)

## Wipe Logic (Implementation details, variable + tag approach, test results)

## CI/CD Integration (Workflow architecture, setup steps, evidence of automated deployments)

## Testing Results (All test scenarios, idempotency verification, application accessibility)

## Challenges & Solutions (Difficulties encountered and how you solved them)

## Research Answers (All research questions answered with analysis)

### 1.3

Q1: What happens if rescue block also fails?
Q2: Can you have nested blocks?
Q3: How do tags inherit to tasks within blocks?

### 2.3

Q1: What's the difference between restart: always and restart: unless-stopped?
Q2: How do Docker Compose networks differ from Docker bridge networks?
Q3: Can you reference Ansible Vault variables in the template?

### 2.5

Q1: Look up community.docker.docker_compose_v2 module
Q2: Compare state: present vs other state options
Q3: Understand recreate parameter options

### 3.6

Q1: Why use both variable AND tag? (Double safety mechanism)
Q2: What's the difference between never tag and this approach?
Q3: Why must wipe logic come BEFORE deployment in main.yml? (Clean reinstall scenario)
Q4: When would you want clean reinstallation vs. rolling update?
Q5: How would you extend this to wipe Docker images and volumes too?

### 4.10

Q1: What are the security implications of storing SSH keys in GitHub Secrets?
Q2: How would you implement a staging → production deployment pipeline?
Q3: What would you add to make rollbacks possible?
Q4: How does self-hosted runner improve security compared to GitHub-hosted?