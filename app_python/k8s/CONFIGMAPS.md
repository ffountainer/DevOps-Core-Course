# Documentation

## Application Changes

### Description of visits counter implementation
### New endpoint documentation
### Local testing evidence with Docker

Here you can see the counter value persistence across restarts.
![](./../docs/screenshots/lab12-shots/counter.png)

## ConfigMap Implementation

### ConfigMap template structure
### config.json content
### How ConfigMap is mounted as file
### How ConfigMap provides environment variables
### Verification outputs
- File content inside pod (cat /config/config.json)

```bash
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl exec mysecretrelease-app-python-696f97599c-5llgh -- cat /config/config.json
Defaulted container "app-python" out of: app-python, vault-agent, vault-agent-init (init)
{
  "app_name": "my-app",
  "environment": "dev",
  "feature_flags": {
    "debug": true,
    "metrics": true
  },
  "settings": {
    "log_level": "info"
  }
}%   
```

- Environment variables in pod

```bash
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl exec mysecretrelease-app-python-696f97599c-5llgh -- printenv | grep APP_   
Defaulted container "app-python" out of: app-python, vault-agent, vault-agent-init (init)
APP_ENV=dev
APP_NAME=my-app
MYSECRETRELEASE_APP_PYTHON_SERVICE_SERVICE_PORT=80
MYSECRETRELEASE_APP_PYTHON_SERVICE_PORT_80_TCP=tcp://10.103.123.105:80
MYSECRETRELEASE_APP_PYTHON_SERVICE_PORT_80_TCP_PROTO=tcp
MYSECRETRELEASE_APP_PYTHON_SERVICE_PORT_80_TCP_PORT=80
MYSECRETRELEASE_APP_PYTHON_SERVICE_SERVICE_HOST=10.103.123.105
MYSECRETRELEASE_APP_PYTHON_SERVICE_PORT=tcp://10.103.123.105:80
MYSECRETRELEASE_APP_PYTHON_SERVICE_PORT_80_TCP_ADDR=10.103.123.105
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl exec mysecretrelease-app-python-696f97599c-5llgh -- printenv | grep LOG_LEVEL
Defaulted container "app-python" out of: app-python, vault-agent, vault-agent-init (init)
LOG_LEVEL=info
(devops) fountainer@Veronicas-MacBook-Air app_python % 
```


## Persistent Volume

### PVC configuration explanation
### Access modes and storage class discussion
### Volume mount configuration
### Persistence test evidence:

```bash
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl exec mysecretrelease-app-python-7b6579656c-z6r7b -- cat /app/data/visits
Defaulted container "app-python" out of: app-python, vault-agent, vault-agent-init (init)
22%                                                                                                                                             
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl delete pod mysecretrelease-app-python-7b6579656c-z6r7b
pod "mysecretrelease-app-python-7b6579656c-z6r7b" deleted
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl get pod
NAME                                          READY   STATUS    RESTARTS      AGE
mysecretrelease-app-python-7b6579656c-b2tzf   2/2     Running   0             60s
vault-0                                       1/1     Running   3 (84m ago)   8d
vault-agent-injector-848dd747d7-qvgl2         1/1     Running   3 (85m ago)   8d
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl exec mysecretrelease-app-python-7b6579656c-b2tzf -- cat /app/data/visits
Defaulted container "app-python" out of: app-python, vault-agent, vault-agent-init (init)
22%                                                                                                                                             
(devops) fountainer@Veronicas-MacBook-Air app_python % 
```

## ConfigMap vs Secret

### When to use ConfigMap
### When to use Secret
### Key differences

## Additional Outputs:

### kubectl get configmap,pvc output

```bash
(devops) fountainer@Veronicas-MacBook-Air app_python % kubectl get configmap,pvc
NAME                                          DATA   AGE
configmap/kube-root-ca.crt                    1      22d
configmap/mysecretrelease-app-python-config   1      7m2s
configmap/mysecretrelease-app-python-env      3      7m2s

NAME                                                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/mysecretrelease-app-python-data   Bound    pvc-42d4685f-8463-4434-8959-0bacd5d972b6   100Mi      RWO            standard       <unset>                 7m2s
(devops) fountainer@Veronicas-MacBook-Air app_python % 
```


