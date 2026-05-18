# Lab 5: Prometheus and Grafana

## Step 1: Create Prometheus File
### Dashboard Tasks

### Commands
```bash
cd Documents
mkdir monitoring
cd monitoring
nano prometheus.yml
```

```file:prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "nginx"
    static_configs:
      - targets: ["nginx-exporter:9113"]
```

## Step 2: Create Docker Compose File
### Dashboard Tasks

### Commands
```bash
nano docker-compose.yml
```

```file:docker-compose.yml
version: '3'

services:
  prometheus:
    image: prom/prometheus
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3000:3000"

  nginx:
    image: nginx
    container_name: nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf

  nginx-exporter:
    image: nginx/nginx-prometheus-exporter
    container_name: nginx-exporter
    command:
      - -nginx.scrape-uri=http://nginx/nginx_status
    ports:
      - "9113:9113"
    depends_on:
      - nginx
```

## Step 3: Start Containers
### Dashboard Tasks
1. Open http://localhost:9090
2. Open http://localhost:3000
3. Grafana username=admin and password=admin

### Commands
```bash
sudo docker compose up -d
```

## Step 4: Monitor Nginx using Grafana
### Dashboard Tasks
1. Go to connections -> Data Sources -> Add data source
2. Pick Prometheus 
3. Change URL to http://prometheus:9090
4. Click save and Test
5. Select the data source required
6. (Alternative) take prebuilt nginx exporter from dashboard using ID 12708


### Commands
```bash
for i in {1..50}; do curl http://localhost; done
sudo docker compose down
```