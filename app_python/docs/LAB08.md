# Documentation

## Architecture - Diagram showing metric flow (app → Prometheus → Grafana)

### Comparison: metrics vs logs (Lab 7) - when to use each

- we use logs to see what has happened and metric to see the quantities: how much and how often.

## Application Instrumentation - What metrics you added and why

### Screenshot of /metrics endpoint output

![](./screenshots/lab08-shots/metrics%20for%20app%20logs.png)

### Code showing metric definitions

- you can see it in app.py
- sections: imports updated, Counter, Histogram, Gauge metrics defined, before request/after request decorators, metrics route decorator

### Documentation explaining your metric choices

- http_requests_total counts how many requests hit the service, so i can see overall traffic and usage patterns
- http_request_duration_seconds measures how long requests take, which helps spot slow endpoints or performance issues
- http_requests_in_progress tracks how many requests are being processed right now, useful for detecting load spikes
- endpoint_calls tracks how often each endpoint is used, so i can understand which parts of the service are actually used
- system_info_duration measures how long it takes to collect system info, mainly to check if that logic becomes slow over time

## Prometheus Configuration - Scrape targets, intervals, retention

### Screenshot of /targets page showing all targets UP

![](./screenshots/lab08-shots/prometheous%20targets.png)

### Screenshot of a successful PromQL query

![](./screenshots/lab08-shots/successful%20query.png)

### prometheus.yml configuration file

- you can find it in ./app_python_monitoring/prometheous/prometheous.yml

## Dashboard Walkthrough - Each panel's purpose and query

### Screenshots of dashboards with live data

### Screenshot showing all 6+ panels working

### Exported dashboard JSON file

## PromQL Examples - 5+ queries with explanations

### PromQL queries that demonstrate RED method

## Production Setup - Health checks, resources, retention policies

### Proof of all services healthy and scraping

### docker compose ps showing all services healthy

### Documentation of retention policies

### Proof of data persistence after restart

## Testing Results - Screenshots showing everything working

## Challenges & Solutions - Issues encountered and fixes