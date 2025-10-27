# Task Management System with DevOps Automation

A Flask-based Todo application with complete CI/CD pipeline using:
- Docker for containerization
- Kubernetes for orchestration
- GitHub Actions for automation

## Features
- Create, Read, Update, and Delete tasks
- Persistent storage using SQLite
- Docker containerization
- Kubernetes deployment
- Automated CI/CD pipeline

## Technology Stack
- Python/Flask
- SQLite
- Docker
- Kubernetes
- GitHub Actions

## CI/CD Pipeline
- Automated builds on push to main branch
- Docker image creation and push to Docker Hub
- Automated deployment to Kubernetes cluster
- Persistent storage using PV and PVC

## Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

## Docker Deployment
```bash
docker build -t todo-app .
docker run -p 5000:5000 todo-app
```

## Kubernetes Deployment
```bash
kubectl apply -f kubernetes/
```

## Accessing the Application
- Local: http://localhost:5000
- Kubernetes: Check service IP using `kubectl get svc todo-app-service`
# Trigger build Mon Oct 27 09:11:00 UTC 2025
# Trigger rebuild Mon Oct 27 09:12:42 UTC 2025
# Trigger rebuild Mon Oct 27 09:14:17 UTC 2025
