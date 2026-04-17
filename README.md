# Real-Time Transaction Monitoring System

A real-time fraud detection pipeline built using Python, Kafka, and Azure.

This project simulates financial transactions, streams them through Kafka, and processes them in real-time to detect potential fraud using rule-based logic.

---

## 🧱 Architecture

Producer → Kafka → Consumer → Fraud Detection → (PostgreSQL - planned)

- Producer generates fake transactions
- Kafka streams events in real-time
- Consumer processes transactions
- Fraud Engine applies detection rules

---

## ⚙️ Tech Stack

- Python
- Apache Kafka
- Docker (Kafka, Zookeeper, PostgreSQL)
- Azure Virtual Machine
- Bicep (Infrastructure as Code)
- Faker (data simulation)

---

## 🚀 How It Works

1. Transactions are generated using Faker
2. Producer publishes transactions to Kafka
3. Consumer reads messages in real-time
4. Fraud rules are applied:
   - High transaction amounts
   - Suspicious country changes
   - Rapid transaction frequency
5. Alerts are logged for suspicious activity

---

## ▶️ Running the Project

This project can run:

### Option 1: Locally
- Start Docker services
- Run producer and consumer

### Option 2: Azure VM (recommended for low-resource machines)
- Deploy VM using Bicep
- SSH into VM
- Clone repo on the VM
- Make the bootstrap script executable: `chmod +x ./infra/bootstrap-vm.sh`
- Run the VM bootstrap script: `./infra/bootstrap-vm.sh`
  - Or from Windows PowerShell run: `.
\infra\bootstrap-vm.ps1 -PublicIp <PUBLIC_IP>`
- Start producer and consumer

For detailed steps, see RUNBOOK.md

---

## 🧠 Key Learnings

- Built an event-driven architecture using Kafka
- Implemented real-time fraud detection logic
- Used Docker for reproducible environments
- Deployed infrastructure using Bicep (IaC)
- Managed cloud resources using ephemeral environments
- Debugged distributed systems (producer/consumer/Kafka)

---

## 🚀 Future Improvements

- Persist transactions and alerts to PostgreSQL
- Add fraud scoring engine (not just rules)
- Build real-time dashboards
- Migrate to Azure Container Apps
- Add CI/CD pipelines (GitHub Actions / Azure DevOps)

---

## 📌 Author

Thabo Mndebele  
Software Engineer | Data Engineering Enthusiast


