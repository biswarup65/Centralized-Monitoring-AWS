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
## 📊 Monitoring
```bash
CloudWatch Dashboards for:

EC2 CPU Utilization

EC2 Memory Utilization (via CloudWatch Agent)

ALB Request Count

Healthy & Unhealthy Target Count

ASG Instance Count
```

## 🚨 Alerting
``` bash
High CPU utilization alarm (> 50%)

Unhealthy target detection

Auto Scaling activity tracking

Email notifications via SNS
```
## 📁 Log Management
```bash
Application & system logs sent to CloudWatch Logs

Centralized log storage in Amazon S3

Amazon S3 for centralized log storage

IAM roles for secure access
```

---

## ⚙️ Implementation Steps 

1️⃣ Created IAM role with CloudWatch and SSM permissions

2️⃣ Launched EC2 instances with CloudWatch Agent installed

3️⃣ Configured Application Load Balancer and Target Groups

4️⃣ Created Auto Scaling Group with CPU-based scaling policy

5️⃣ Built CloudWatch dashboards for centralized visibility

6️⃣ Configured CloudWatch alarms and SNS notifications

7️⃣ Exported logs from CloudWatch Logs to Amazon S3

8️⃣ Tested alarms using CPU stress simulation

---

## 🖼️ CloudWatch Dashboard & AWS Console Snapshots

## 📊 CloudWatch Centralized Dashboard

![CloudWatch Dashboard](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/cw-custom-dashboard.png)

---

## 📈 EC2 Instance CPU Metrics

![EC2 CPU Metrics](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/cpu-utilization-metrics-graph.png)

---

## 📢 CloudWatch Alarms (Triggered / OK State)

## 🔔 CPU Utilization Alarm

![CPU Utilization Alarm](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/cpu-utilization-cw.png)

---

![CPU Utilization Alert](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/cw-alert-cpu-utilization.png)

---

## 🔔 Unhealthy target Alarms

![Unhealthy target Alarm-1](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/unhealthy-host-count-alarm-1.png)

---

![Unhealthy target Alarm-2](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/unhealthy-host-count-alarm-2.png)

---

![Unhealthy target Alert](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/cw-alert-unhealthy-hostCount.png)

---

## 🔔 Auto Scaling Group Scaling Event Alarm

![ASG Scaling event alarm](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/asg-scaling-event-cw-graph.png)

---

## 📜 Auto Scaling Group Activity History

![ASG Activity History](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/asg-activity-history.png)

---

## 📁 S3 Logs Bucket

![S3 Logs Bucket](https://github.com/biswarup65/Centralized-Monitoring-AWS/blob/main/screenshots/s3-bucket-logs.png)

---

## 🧪 Testing & Validation

▪ CPU stress testing triggered CloudWatch alarms

▪ ASG scaled out based on CPU utilization

▪ ALB health checks detected unhealthy instances

▪ Dashboard metrics updated in real time

---

## ✅ Conclusion

This project demonstrates a **practical, monitoring and alerting AWS infrastructure** using Amazon CloudWatch. By implementing centralized dashboards, proactive alarms, Auto Scaling activity tracking, and centralized log storage in Amazon S3, the solution provides **real-time visibility and early incident detection** across EC2, ALB, and ASG resources.

It reflects **real-world cloud support responsibilities**, showcasing skills in system observability, alert handling, and operational monitoring.







