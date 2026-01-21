# 📊 Centralized Monitoring & Alerting System for AWS Infrastructure

![Project Architecture]()

## 📌 Project Overview

This project implements a centralized monitoring and alerting system for AWS infrastructure using Amazon CloudWatch.
It focuses purely on monitoring, alerting, and visibility, which are core responsibilities of Cloud Engineers.

The system monitors EC2 instances behind an Application Load Balancer and Auto Scaling Group, triggers alarms on critical events, and stores logs centrally in Amazon S3.
---

## 🏗️ Architecture Overview

• EC2 instances running a web application

• Application Load Balancer (ALB)

• Auto Scaling Group (ASG)

• Amazon CloudWatch (metrics, alarms, dashboards)

---
## 🔧 AWS Services Used

✅ Amazon EC2

✅ Amazon CloudWatch

✅ Auto Scaling Group (ASG)

✅ Elastic Load Balancer (ALB)

✅ AWS Identity and Access Management (IAM)

✅ Amazon S3
---

## 🎯 Key Features
📊 Monitoring

CloudWatch Dashboards for:

EC2 CPU Utilization

EC2 Memory Utilization (via CloudWatch Agent)

ALB Request Count

Healthy & Unhealthy Target Count

ASG Instance Count

🚨 Alerting

High CPU utilization alarm (> 50%)

Unhealthy target detection

Auto Scaling activity tracking

Email notifications via SNS

📁 Log Management

Application & system logs sent to CloudWatch Logs

Centralized log storage in Amazon S3
---

Amazon S3 for centralized log storage

IAM roles for secure access
