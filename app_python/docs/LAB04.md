# Documentation

### Cloud Provider & Infrastructure

## Task 1 (Terraform implementation)

### Cloud provider chosen and why
I chose Yandex Cloud since it provides solid resource provision with a lot of RAM and storage space, also it has a free trial period.

### Terraform version used

Terraform v1.14.5 on darwin_arm64

### Project structure explanation

### Key configuration decisions

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

```bash
ssh -i /home-directory/.ssh/terraform-vm-key ubuntu@62.84.117.91
```

### Terminal output from terraform plan and terraform apply

![Plan](./screenshots/lab04-shots/terraform%20plan.png)

![Apply-1](./screenshots/lab04-shots/terraform%20apply-1.png)

![Apply-2](./screenshots/lab04-shots/terraform%20apply-2.png)

### Proof of SSH access to VM

![SSH](./screenshots/lab04-shots/ssh%20output%20terraform.png)

### Challenges encountered

## Task 2 (Pulumi Implementation)

### Pulumi version and language used

### Terraform destroy output

![](./screenshots/lab04-shots/terraform%20destroy.png)

### How code differs from Terraform

### Advantages you discovered

### Challenges encountered

### Terminal output

- pulumi preview

- pulumi up

- SSH connection to VM

### Public IP of Pulumi-created VM

## Terraform vs Pulumi Comparison

### Code differences (HCL vs Python/TypeScript)

### Which tool you prefer and why

## Lab 5 Preparation & Cleanup

