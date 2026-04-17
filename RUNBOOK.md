

# RUNBOOK: Real-Time Transaction Monitoring System

This guide explains how to deploy, run, and troubleshoot the system after each redeployment.

---

# FULL WORKFLOW (After Every Redeploy)

---

## 1. Get VM Public IP

```powershell
az vm list -d -g rttm-rg -o table
````

Copy the PublicIps value.

---

## 2. SSH into VM

```powershell
ssh -i $HOME\.ssh\rttm_vm_key azureuser@<PUBLIC_IP>
```

---

## 3. Clone Repo (if fresh VM)

```bash
git clone https://github.com/mndebelelt/real-time-transaction-monitoring.git
cd real-time-transaction-monitoring
```

---

## 4. Bootstrap the VM (recommended)

From the repo root on the VM, make the script executable and run it:

```bash
chmod +x ./infra/bootstrap-vm.sh
./infra/bootstrap-vm.sh
```

Or from a Windows host, run this from the local repo root:

```powershell
.\infra\bootstrap-vm.ps1 -PublicIp <PUBLIC_IP>
```

This script will:
- install Docker if needed
- install Docker Compose or the compose plugin
- start Kafka, Zookeeper, and Postgres
- install Python dependencies

If you prefer to run the steps manually, use:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable --now docker
```

If your VM does not support the plugin command, install the legacy package:

```bash
sudo apt install -y docker-compose
```

---

## 5. Start Infrastructure (MANDATORY)

```bash
cd docker
docker compose up -d
# or, if using legacy Docker Compose:
# docker-compose up -d
docker ps
```

Expected containers:

* rttm-kafka
* rttm-zookeeper
* rttm-postgres

---

## Why Docker is required

VM = empty machine
Docker = runs Kafka and Postgres

You must start Docker services after every redeploy.

---

## 6. Install Python Dependencies

```bash
cd ~/real-time-transaction-monitoring
pip3 install -r requirements.txt
```

---

## 7. Run Producer

(Open SSH session 1)

```bash
python3 -m app.producer.run_producer
```

---

## 7. Run Consumer

(Open SSH session 2)

```bash
python3 -m app.consumer.run_consumer
```

---

## 8. Expected Output

Producer:

```
Published transaction...
```

Consumer:

```
Processed transaction...
FRAUD DETECTED...
```

---

# Architecture

```
Azure VM
 ├── Docker (Kafka, Zookeeper, Postgres)
 └── Python (Producer + Consumer)
```

---

# Common Issues & Fixes

---

## SSH Connection Refused

Cause:

* VM recreated → IP changed

Fix:

```powershell
az vm list -d -g rttm-rg -o table
```

---

## Kafka Connection Errors

Cause:

* Docker not running

Fix:

```bash
docker-compose up -d
```


# Destroy Environment (Save Costs)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\destroy.ps1
```

---

# Key Concepts

VM = host machine
Docker = runs services

Destroy → Recreate → New IP

Deploy → Use → Destroy

---

# Future Work

* Store transactions in PostgreSQL
* Add fraud scoring
* Replace VM with Container Apps
* Add monitoring & logging

```

