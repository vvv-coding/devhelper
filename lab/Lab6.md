# Lab 6: Ansible and Terraform

## Step 1: Terraform and Ansible Installation
### Dashboard Tasks

### Commands
```bash
sudo apt update

sudo snap install terraform --classic
sudo apt install ansible -y

terraform --version
ansible --version
```

## Step 2: Running Terraform and Ansible
### Dashboard Tasks
1. Visit http://localhost:8080
2. Visit http://localhost:8080

### Commands
```bash
sudo docker ps -a
sudo docker rm nginx-container-id
sudo docker rmi nginx

cd Documents
mkdir terraform-nginx
cd terraform-nginx
nano main.tf
```

```file:main.tf
terraform {
 required_providers {
  docker = {
   source = "kreuzwerker/docker"
   version = "~> 3.0"
  }
 }
}

provider "docker" {}

resource "docker_container" "nginx" {
 name = "nginx_container"
 image = "nginx:latest"
 
 ports {
  internal = 80
  external = 8080
 }
}
```

## Step 3: Initialize Terraform and Create Playbook
### Dashboard Tasks

### Commands
```bash
terraform init

sudo terraform apply

cd ..
mkdir ansible
cd ansible
nano index.html
```

```file:index.html
<h1>DevOps Lab</h1>
<p>This page is configured using Ansible</p>
```

```bash
nano homepage.yml
```

```file:homepage.yml
- name: Change nginx homepage
  hosts: localhost
  
  tasks:
  
- name: Copy HTML into container
  command: docker cp index.html nginx_container:/usr/share/nginx/html/index.html
```

```bash
sudo anisble-playbook homepage.yml
sudo terraform destroy
```

## Step 4: Create Alert Rule
### Dashboard Tasks
1. rate(prometheus_http_requests_total[1m])
2. rate(nginx_http_requests_total[1m])
3. Configure threshold

### Commands
```bash
sudo docker compose up -d

for i in {1..1000}
do
curl http://localhost:9090
done

for i in {1..1000}
do
curl http://localhost
done
```