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

- in pod I have correct env vars:

```bash
(devops) fountainer@Veronicas-MacBook-Air DevOps-Core-Course % kubectl exec -it mysecretrelease-app-python-7975557578-6zc9m -- sh
$ echo $PASSWORD
mypass293i20@@nekf
$ echo $USERNAME
fountainer
```

- and outside the secrets are hidden

from ```bash kubectl describe pod mysecretrelease-app-python-7975557578-6zc9m```

```bash
Environment:
      PASSWORD:  <set to the key 'password' in secret 'app-credentials'>  Optional: false
      USERNAME:  <set to the key 'username' in secret 'app-credentials'>  Optional: false
```


## Resource Management

### Resource limits configuration

```bash
resources:
    requests:
        cpu: {{ .Values.resources.requests.cpu }}
        memory: {{ .Values.resources.requests.memory }}
    limits:
        cpu: {{ .Values.resources.limits.cpu }}
        memory: {{ .Values.resources.limits.memory }}
```
- in values.yaml I have

```bash
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "256Mi"
```

### Explanation of requests vs limits

- requests is a setting that shows kubernates how much resources are needed for a container to run
- limits show how much resources a container is allowed to use (max)

### How to choose appropriate values

- you should analyze what processes does your container run and how many cpu/memory it may need 
- values can be adjusted by observing the running container
- if you have multiple containers/pods you should constraint them in such a way that they all can work without throttling
- if the memory limit is too low the container can be killed right away

## Vault Integration

### Vault installation verification (kubectl get pods)
### Policy and role configuration (sanitized)
### Proof of secret injection (show file exists, path structure)
### Explanation of the sidecar injection pattern

## Security Analysis

### Comparison: K8s Secrets vs Vault
### When to use each approach
### Production recommendations

