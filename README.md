# 🚀 Job Alert Bot

A lightweight automation project that monitors job listings and sends email notifications when new postings are detected.

---

## 📌 Overview

**Job Alert Bot** is a simple Python automation script that:

* Scrapes job listings
* Detects new postings
* Sends email alerts
* Runs automatically every day at **09:00** via GitHub Actions
* Is containerized using Docker

> No VPS or dedicated server required.

---

## ⚙️ CI/CD Pipeline

Triggered on push to `main` branch:

1. Install dependencies
2. Run lint checks (flake8)
3. Build Docker image
4. Push image to Docker Hub

---

## ⏰ Scheduled Workflow

Triggered daily using cron:

1. Runs the job alert script
2. Sends email if new listings are found
3. Fails the workflow if an error occurs

Workflow failures are monitored via GitHub notification emails.

---

## 🔐 Secrets Management

Sensitive credentials are stored securely using GitHub Secrets:

* `EMAIL_ADDRESS`
* `EMAIL_PASSWORD`
* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`

No credentials are stored in the repository.

---

## 🛠 Tech Stack

* Python 3.11
* requests
* beautifulsoup4
* Docker
* GitHub Actions

---

## 🎯 Project Goal

This project demonstrates:

* Basic CI/CD implementation
* Docker-based deployment
* Scheduled automation with GitHub Actions
* Lightweight monitoring without external infrastructure

---

👤 **Mine Kırmacı-Junior DevOps Engineer**
