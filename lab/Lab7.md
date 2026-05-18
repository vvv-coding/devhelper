# Lab 7: Docker Networking

## Step 1: Create two Ubuntu container on the Default Bridge
### Dashboard Tasks

### Commands
```bash
docker network ls

apt-get install bridge-utils
brctl show

docker run -dt ubuntu bash
docker inspect [network_id]
```

## Step 2: Ping Container 2 from Container 1
### Dashboard Tasks

### Commands
```bash
docker exec -it 3bf108d1
apt-get install iputils-ping
ping google.com

ping 172.17.0.3
```

## Step 3: Create Custom Bridge
### Dashboard Tasks

### Commands
```bash
docker network create custom_bridge
docker run -dt --network custom_bridge ubuntu bash
docker run -dt --network custom_bridge ubuntu bash
docker inspect 291da8a0175a
```

## Step 4: Connecting container in default bridge to custom bridge
### Dashboard Tasks

### Commands
```bash
docker network connect custom_bridge 3bf108d121161096
docker inspect custom_bridge
docker network disconnect custom_bridge 3bf108d121161096
```