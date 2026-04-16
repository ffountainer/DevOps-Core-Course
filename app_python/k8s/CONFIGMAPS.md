# Documentation

## Application Changes

###  Description of visits counter implementation
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
    - Counter value before pod deletion
    - Pod deletion command
    - Counter value after new pod starts

## ConfigMap vs Secret

### When to use ConfigMap
### When to use Secret
### Key differences

## Required Screenshots/Outputs:

### kubectl get configmap,pvc output


