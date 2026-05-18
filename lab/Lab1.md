# Lab 1: Docker Basics

## Step 1: Check existing docker images
### Dashboard Tasks

### Commands
```bash
sudo su - 
docker images
```

## Step 2: Run existing docker images
### Dashboard Tasks

### Commands
```bash
docker run hello-world
```

## Step 3: Pull Docker Image from Docker Hub
### Dashboard Tasks

### Commands
```bash
docker pull nginx
```

## Step 4: Run docker image as a container
### Dashboard Tasks

### Commands
```bash
docker run -d -p 8000:80 nginx
```

## Step 5: Check container ID
### Dashboard Tasks
 
### Commands
```bash
docker ps
```


## Step 6: Stop the container
### Dashboard Tasks

### Commands
```bash
docker stop [container_id]
```


## Step 7: Start the container
### Dashboard Tasks

### Commands
```bash
docker start [image_name]
```

## Step 8: Delete the container
### Dashboard Tasks

### Commands
```bash
docker rm container_id
```

## Step 9: Execution inside the Docker Container
### Dashboard Tasks

### Commands
```bash
docker exec -it my-nginx bash
```

## Step 10: Change contents of default nginx page
### Dashboard Tasks

### Commands
```bash
cd /usr/share/nginx/html
nano index.html
```

```file:index.html
<h1>My Custom Page</h1>
<p>By [NAME]</p>
```

## Step 11: Stop and Delete
### Dashboard Tasks

### Commands
```bash
docker stop [container_id]
docker rm [container_id]
docker rmi [image_id]
```