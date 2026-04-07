# Documentation

## Kubernetes Secrets

### Output of creating and viewing your secret

```bash
(devops) fountainer@Veronicas-MacBook-Air DevOps-Core-Course % kubectl create secret generic app-credentials --from-literal=username=fountainer --from-literal=password=‘mypass293i20@@nekf’
secret/app-credentials created
(devops) fountainer@Veronicas-MacBook-Air DevOps-Core-Course % kubectl get secret app-credentials  -o yaml
apiVersion: v1
data:
  password: 4oCYbXlwYXNzMjkzaTIwQEBuZWtm4oCZ
  username: Zm91bnRhaW5lcg==
kind: Secret
metadata:
  creationTimestamp: "2026-04-07T14:46:16Z"
  name: app-credentials
  namespace: default
  resourceVersion: "24859"
  uid: 6997ca85-68fa-4278-9d51-a6531df977e9
type: Opaque
```
### Decoded secret values demonstration

```bash
(devops) fountainer@Veronicas-MacBook-Air DevOps-Core-Course % echo "4oCYbXlwYXNzMjkzaTIwQEBuZWtm4oCZ" | base64 -d
‘mypass293i20@@nekf’%                                                                                                                                                    
(devops) fountainer@Veronicas-MacBook-Air DevOps-Core-Course % echo "Zm91bnRhaW5lcg==" | base64 -d
fountainer% 
```
### Explanation of base64 encoding vs encryption

- Encoding is when we use some publicly accesible algorithm to encode our data. The goal is keeping integrity and usability of the data, it is not really about security.

- In turn, Encryption is about securuty. It envolves encrypting with an algorithm that can be only resolved by a user who has an encryption key. 

## Helm Secret Integration

### Chart structure showing secrets.yaml
### How secrets are consumed in deployment
### Verification output (env vars in pod, excluding actual values)

## Resource Management

### Resource limits configuration
### Explanation of requests vs limits
### How to choose appropriate values

## Vault Integration

### Vault installation verification (kubectl get pods)
### Policy and role configuration (sanitized)
### Proof of secret injection (show file exists, path structure)
### Explanation of the sidecar injection pattern

## Security Analysis

### Comparison: K8s Secrets vs Vault
### When to use each approach
### Production recommendations

