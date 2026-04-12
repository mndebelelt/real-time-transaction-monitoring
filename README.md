# Real-Time Transaction Monitoring

A local streaming data engineering project built with Python, Kafka, and PostgreSQL.

## Overview

This project simulates transaction events, streams them through Kafka, evaluates suspicious activity in near real time, and stores both transactions and generated alerts in PostgreSQL.

## Goals

- Learn streaming fundamentals
- Practice Kafka producers and consumers
- Build a clean Python data engineering project
- Store and analyze streaming events
- Create a strong GitHub portfolio project

## Tech Stack

- Python
- Kafka
- PostgreSQL
- Docker Compose
- Pytest

## Planned Features

- Transaction generator
- Kafka producer
- Kafka consumer
- Rule-based alert detection
- PostgreSQL persistence
- Tests
- Documentation
- Dashboard later

## Project Structure

```text
real-time-transaction-monitoring/
│
├── app/
│   ├── producer/
│   ├── consumer/
│   └── common/
│
├── database/
├── docker/
├── tests/
├── docs/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md