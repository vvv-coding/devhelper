# Lab 8: Kubernetes

## Step 1: Install Kubernetes
### Dashboard Tasks

### Commands
```bash
sudo apt update

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

## Step 2: Install Minikube
### Dashboard Tasks

### Commands
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube version

sudo usermod -aG docker $USER
newgrp docker
minikube start --driver=docker

minikube status
# If clash with Jenkins
kubectl config use-context minikube
kubectl get nodes
```

## Step 3: Create Pod
### Dashboard Tasks

### Commands
```bash
kubectl run my-pod --image=nginx --restart=Never
kubectl get pod my-pod -o wide
```

## Step 4: Expose your pod through NodePort Service
### Dashboard Tasks
1. Try to access nginx server through service IP address only once the service shows Running

### Commands
```bash
kubectl expose pod my-pod --type=NodePort --port=80 --name=my-service
kubectl get services
minikube service my-service --url
```

## Step 5: Delete Pod and Service
### Dashboard Tasks

### Commands
```bash
kubectl delete service my-service
kubectl delete pod my-pod
```

## Step 6: Deployment
### Dashboard Tasks

### Commands
```bash
kubectl create deployment my-deployment --image=nginx --replicas=2
kubectl get deployment
kubectl expose deployment my-deployment --type=NodePort --port=80
minikube service my-deployment
minikube service my-deployment --url
kubectl scale deployment my-deployment --replica=5
```

## Step 7: Delete Deployment
### Dashboard Tasks

### Commands
```bash
kubectl delete deployment my-deployment
minikube stop
```