# Documentation
## Task 1

### Cloud provider chosen and why
I chose Yandex Cloud since it provides solid resource provision with a lot of RAM and storage space, also it has a free trial period.

### Terraform version used

Terraform v1.14.5 on darwin_arm64

### Resources created (VM size, region, etc.)

- service account

- boot disk with ubuntu image

- vm (2 cores, 2 memory)

- network

- subnet (zone ru-central1-a)

- security group

### Public IP address of created VM

```bash
external_ip_address_vm = "62.84.117.91"
```

### SSH connection command

### Terminal output from terraform plan and terraform apply

![Plan](./screenshots/lab04-shots/terraform%20plan.png)

![Apply-1](./screenshots/lab04-shots/terraform%20apply-1.png)

![Apply-2](./screenshots/lab04-shots/terraform%20apply-2.png)

### Proof of SSH access to VM
