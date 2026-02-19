## SETUP INSTRUCTIONS: PULUMI

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### Install Pulumi and Yandex provider
```bash
pip install "pulumi>=3.0.0,<4.0.0" pulumi-yandex
```

### Login to Pulumi (choose Pulumi Cloud or local backend)
```bash
pulumi login
```

### Initialize new Python project
```bash
pulumi new python
```

### Configure provider (generic placeholders)
```bash
pulumi config set yandex:token <YOUR_YC_TOKEN> --secret
pulumi config set yandex:cloud-id <YOUR_CLOUD_ID>
pulumi config set yandex:folder-id <YOUR_FOLDER_ID>
pulumi config set zone <YOUR_ZONE>
pulumi config set ssh_key_path <PATH_TO_PUBLIC_SSH_KEY>
pulumi config set ssh_source_ip <YOUR_IP_CIDR>
pulumi config set app_port <APP_PORT_NUMBER>
```

### Write __main__.py defining:
### - VPC / Network
### - Subnet
### - Security Group / Firewall rules
### - Disk
### - VM / Compute Instance

### Preview and apply infrastructure
```bash
pulumi preview
pulumi up
```

### Access VM via SSH (use your private key)
```bash
ssh -i <PATH_TO_PRIVATE_SSH_KEY> ubuntu@<EXTERNAL_VM_IP>
```

### Destroy infrastructure when done
```bash
pulumi destroy
```
