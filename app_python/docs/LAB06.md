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

### First run

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/deploy.yml --extra-vars @./group_vars/all.yml

PLAY [Deploy application] *****************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
ok: [terraform]

TASK [docker : Install prerequisites] *****************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker GPG key] ********************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker APT repository] *************************************************************************************************************************
[WARNING]: Deprecation warnings can be disabled by setting `deprecation_warnings=False` in ansible.cfg.
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/docker/defaults/main.yml:7:14

5 docker_user: "ubuntu"
6 docker_gpg_url: "https://download.docker.com/linux/ubuntu/gpg"
7 docker_repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
               ^ column 14

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

ok: [terraform]

TASK [docker : Install Docker packages] ***************************************************************************************************************************
ok: [terraform]

TASK [docker : Install python3-docker for Ansible Docker modules] *************************************************************************************************
ok: [terraform]

TASK [docker : ensure docker service is enabled] ******************************************************************************************************************
ok: [terraform]

TASK [docker : Add user to Docker group] **************************************************************************************************************************
ok: [terraform]

TASK [web_app : Create application directory] *********************************************************************************************************************
ok: [terraform]

TASK [web_app : Template docker-compose.yml] **********************************************************************************************************************
changed: [terraform]

TASK [web_app : Deploy with Docker Compose] ***********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/my-app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
changed: [terraform]

TASK [web_app : Log deployment attempt] ***************************************************************************************************************************
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/main.yml:33:18

31     - name: Log deployment attempt
32       copy:
33         content: "Docker Compose deployment attempted on {{ ansible_date_time.iso8601 }}"
                    ^ column 18

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

changed: [terraform]

PLAY RECAP ********************************************************************************************************************************************************
terraform                  : ok=12   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

### Second run removed "changed" status of some fields (not with the current time)

```bash
TASK [web_app : Template docker-compose.yml] **********************************************************************************************************************
ok: [terraform]

TASK [web_app : Deploy with Docker Compose] ***********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/my-app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
ok: [terraform]
```

clear
### Verifying on target VM

```bash
ubuntu@fhmebroid75qocec3dc3:~$ docker ps
CONTAINER ID   IMAGE                      COMMAND           CREATED          STATUS          PORTS                                           NAMES
7c279d0b3c18   fountainer/my-app:latest   "python app.py"   10 minutes ago   Up 10 minutes   0.0.0.0:1999->12345/tcp, [::]:1999->12345/tcp   my-app-my-app-1
0a0701a21e3a   9582a1fe4631               "python app.py"   25 hours ago     Up 25 hours     0.0.0.0:8080->12345/tcp                         my-app
ubuntu@fhmebroid75qocec3dc3:~$ curl http://localhost:1999
{
  "message": {
    "endpoints": [
      {
        "description": "Service information",
        "method": "GET",
        "path": "/"
      },
      {
        "description": "Health check",
        "method": "GET",
        "path": "/health"
      }
    ],
    "request": {
      "client_ip": "127.0.0.1",
      "method": "GET",
      "path": "/",
      "port": 12345,
      "user_agent": "curl/7.81.0"
    },
    "runtime": {
      "current_time": "2026-01-07T14:30:00.000Z",
      "timezone": "UTC",
      "uptime_human": "1 hour, 0 minutes",
      "uptime_seconds": {
        "human": "0 hours, 0 minutes",
        "seconds": 0
      }
    },
    "service": {
      "debug status": true,
      "description": "DevOps course info service",
      "framework": "Flask",
      "name": "devops-info-service",
      "version": "1.0.0"
    },
    "system": {
      "architecture": "x86_64",
      "cpu_count": 8,
      "hostname": "7c279d0b3c18",
      "platform": "Linux",
      "platform_version": "Ubuntu 24.04",
      "python_version": "3.13.12"
    }
  }
}
ubuntu@fhmebroid75qocec3dc3:~$ 
```

## Wipe Logic (Implementation details, variable + tag approach, test results)

### Scenario 1: Normal deployment (wipe should NOT run)

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/deploy.yml --extra-vars @./group_vars/all.yml

PLAY [Deploy application] *****************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
ok: [terraform]

TASK [docker : Install prerequisites] *****************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker GPG key] ********************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker APT repository] *************************************************************************************************************************
[WARNING]: Deprecation warnings can be disabled by setting `deprecation_warnings=False` in ansible.cfg.
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/docker/defaults/main.yml:7:14

5 docker_user: "ubuntu"
6 docker_gpg_url: "https://download.docker.com/linux/ubuntu/gpg"
7 docker_repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
               ^ column 14

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

ok: [terraform]

TASK [docker : Install Docker packages] ***************************************************************************************************************************
ok: [terraform]

TASK [docker : Install python3-docker for Ansible Docker modules] *************************************************************************************************
ok: [terraform]

TASK [docker : ensure docker service is enabled] ******************************************************************************************************************
ok: [terraform]

TASK [docker : Add user to Docker group] **************************************************************************************************************************
ok: [terraform]

TASK [web_app : Create application directory] *********************************************************************************************************************
ok: [terraform]

TASK [web_app : Template docker-compose.yml] **********************************************************************************************************************
ok: [terraform]

TASK [web_app : Include wipe tasks] *******************************************************************************************************************************
included: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/wipe.yml for terraform

TASK [web_app : Stop and remove containers] ***********************************************************************************************************************
skipping: [terraform]

TASK [web_app : Remove docker-compose file] ***********************************************************************************************************************
skipping: [terraform]

TASK [web_app : Remove application directory] *********************************************************************************************************************
skipping: [terraform]

TASK [web_app : Log wipe completion] ******************************************************************************************************************************
skipping: [terraform]

TASK [web_app : Deploy with Docker Compose] ***********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/my-app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
ok: [terraform]

TASK [web_app : Log deployment attempt] ***************************************************************************************************************************
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/main.yml:38:18

36     - name: Log deployment attempt
37       copy:
38         content: "Docker Compose deployment attempted on {{ ansible_date_time.iso8601 }}"
                    ^ column 18

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

changed: [terraform]

PLAY RECAP ********************************************************************************************************************************************************
terraform                  : ok=13   changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   

(devops) fountainer@Veronicas-MacBook-Air ansible % 
```

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ssh ubuntu@93.77.181.173 "docker ps"
CONTAINER ID   IMAGE                      COMMAND           CREATED          STATUS          PORTS                                           NAMES
7c279d0b3c18   fountainer/my-app:latest   "python app.py"   21 minutes ago   Up 21 minutes   0.0.0.0:1999->12345/tcp, [::]:1999->12345/tcp   my-app-my-app-1
0a0701a21e3a   9582a1fe4631               "python app.py"   25 hours ago     Up 25 hours     0.0.0.0:8080->12345/tcp                         my-app
(devops) fountainer@Veronicas-MacBook-Air ansible % 
```

### Scenario 2: Wipe only (remove existing deployment)

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/deploy.yml -e "web_app_wipe=true" --tags web_app_wipe --extra-vars @./group_vars/all.yml

PLAY [Deploy application] *****************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
ok: [terraform]

TASK [web_app : Include wipe tasks] *******************************************************************************************************************************
included: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/wipe.yml for terraform

TASK [web_app : Stop and remove containers] ***********************************************************************************************************************
[ERROR]: Task failed: Module failed: "/opt/my-app" is not a directory
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/wipe.yml:5:7

3   block:
4
5     - name: Stop and remove containers
        ^ column 7

fatal: [terraform]: FAILED! => {"changed": false, "msg": "\"/opt/my-app\" is not a directory"}
...ignoring

TASK [web_app : Remove docker-compose file] ***********************************************************************************************************************
ok: [terraform]

TASK [web_app : Remove application directory] *********************************************************************************************************************
ok: [terraform]

TASK [web_app : Log wipe completion] ******************************************************************************************************************************
ok: [terraform] => {
    "msg": "Application my-app wiped successfully"
}

PLAY RECAP ********************************************************************************************************************************************************
terraform                  : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
```

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ssh ubuntu@93.77.181.173 "docker ps"               
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
(devops) fountainer@Veronicas-MacBook-Air ansible % ssh ubuntu@93.77.181.173 "ls /opt"                 
containerd
(devops) fountainer@Veronicas-MacBook-Air ansible %
```

### Scenario 3: Clean reinstallation (wipe → deploy)

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/deploy.yml -e "web_app_wipe=true" --extra-vars @./group_vars/all.yml

PLAY [Deploy application] *****************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
ok: [terraform]

TASK [docker : Install prerequisites] *****************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker GPG key] ********************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker APT repository] *************************************************************************************************************************
[WARNING]: Deprecation warnings can be disabled by setting `deprecation_warnings=False` in ansible.cfg.
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/docker/defaults/main.yml:7:14

5 docker_user: "ubuntu"
6 docker_gpg_url: "https://download.docker.com/linux/ubuntu/gpg"
7 docker_repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
               ^ column 14

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

ok: [terraform]

TASK [docker : Install Docker packages] ***************************************************************************************************************************
ok: [terraform]

TASK [docker : Install python3-docker for Ansible Docker modules] *************************************************************************************************
ok: [terraform]

TASK [docker : ensure docker service is enabled] ******************************************************************************************************************
ok: [terraform]

TASK [docker : Add user to Docker group] **************************************************************************************************************************
ok: [terraform]

TASK [web_app : Include wipe tasks] *******************************************************************************************************************************
included: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/wipe.yml for terraform

TASK [web_app : Stop and remove containers] ***********************************************************************************************************************
[ERROR]: Task failed: Module failed: "/opt/my-app" is not a directory
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/wipe.yml:5:7

3   block:
4
5     - name: Stop and remove containers
        ^ column 7

fatal: [terraform]: FAILED! => {"changed": false, "msg": "\"/opt/my-app\" is not a directory"}
...ignoring

TASK [web_app : Remove docker-compose file] ***********************************************************************************************************************
ok: [terraform]

TASK [web_app : Remove application directory] *********************************************************************************************************************
ok: [terraform]

TASK [web_app : Log wipe completion] ******************************************************************************************************************************
ok: [terraform] => {
    "msg": "Application my-app wiped successfully"
}

TASK [web_app : Create application directory] *********************************************************************************************************************
changed: [terraform]

TASK [web_app : Template docker-compose.yml] **********************************************************************************************************************
changed: [terraform]

TASK [web_app : Deploy with Docker Compose] ***********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/my-app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
changed: [terraform]

TASK [web_app : Log deployment attempt] ***************************************************************************************************************************
[DEPRECATION WARNING]: INJECT_FACTS_AS_VARS default to `True` is deprecated, top-level facts will not be auto injected after the change. This feature will be removed from ansible-core version 2.24.
Origin: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/main.yml:37:18

35     - name: Log deployment attempt
36       copy:
37         content: "Docker Compose deployment attempted on {{ ansible_date_time.iso8601 }}"
                    ^ column 18

Use `ansible_facts["fact_name"]` (no `ansible_` prefix) instead.

changed: [terraform]

PLAY RECAP ********************************************************************************************************************************************************
terraform                  : ok=17   changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1 
```

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ssh ubuntu@93.77.181.173 "docker ps"               
CONTAINER ID   IMAGE                      COMMAND           CREATED          STATUS          PORTS                                           NAMES
167ea730bdc1   fountainer/my-app:latest   "python app.py"   20 seconds ago   Up 19 seconds   0.0.0.0:1999->12345/tcp, [::]:1999->12345/tcp   my-app-my-app-1
```
### Safety checks (should NOT wipe)

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/deploy.yml --tags web_app_wipe --extra-vars @./group_vars/all.yml

PLAY [Deploy application] *****************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
ok: [terraform]

TASK [web_app : Include wipe tasks] *******************************************************************************************************************************
included: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/wipe.yml for terraform

TASK [web_app : Stop and remove containers] ***********************************************************************************************************************
skipping: [terraform]

TASK [web_app : Remove docker-compose file] ***********************************************************************************************************************
skipping: [terraform]

TASK [web_app : Remove application directory] *********************************************************************************************************************
skipping: [terraform]

TASK [web_app : Log wipe completion] ******************************************************************************************************************************
skipping: [terraform]

PLAY RECAP ********************************************************************************************************************************************************
terraform                  : ok=2    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   

(devops) fountainer@Veronicas-MacBook-Air ansible % 
```

```bash
(devops) fountainer@Veronicas-MacBook-Air ansible % ansible-playbook playbooks/deploy.yml -e "web_app_wipe=true" --tags web_app_wipe --extra-vars @./group_vars/all.yml

PLAY [Deploy application] *****************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
ok: [terraform]

TASK [web_app : Include wipe tasks] *******************************************************************************************************************************
included: /Users/fountainer/uni/devops/DevOps-Core-Course/app_python/ansible/roles/web_app/tasks/wipe.yml for terraform

TASK [web_app : Stop and remove containers] ***********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/my-app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
changed: [terraform]

TASK [web_app : Remove docker-compose file] ***********************************************************************************************************************
changed: [terraform]

TASK [web_app : Remove application directory] *********************************************************************************************************************
changed: [terraform]

TASK [web_app : Log wipe completion] ******************************************************************************************************************************
ok: [terraform] => {
    "msg": "Application my-app wiped successfully"
}

PLAY RECAP ********************************************************************************************************************************************************
terraform                  : ok=6    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### App running after complete reinstall

![](./screenshots/lab06-shots/app%20running%20after%20clean%20reinstall.png)


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