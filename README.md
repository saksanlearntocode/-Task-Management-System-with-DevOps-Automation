# Task Management System with DevOps Automation

A Flask-based Todo application with complete CI/CD pipeline using:
- Docker for containerization
- Kubernetes for orchestration
- Jenkins for CI/CD pipeline
- GitHub for source control

## Features
- Create, Read, Update, and Delete tasks
- Persistent storage using SQLite
- Docker containerization
- Kubernetes deployment
- Automated CI/CD with Jenkins

## Technology Stack
- Python/Flask
- SQLite
- Docker
- Kubernetes (Minikube)
- Jenkins

## Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access at http://localhost:5000

## Docker Deployment
```bash
# Build the application image
docker build -t todo-app .

# Run the container
docker run -p 5000:5000 todo-app
```

## Kubernetes Deployment
```bash
# Start Minikube if not running
minikube start

# Apply Kubernetes manifests
kubectl apply -f kubernetes/

# Get service URL
minikube service todo-app-service --url
```

## Jenkins CI/CD Setup

### 1. Build Jenkins Container
```bash
# Build custom Jenkins image with Docker and kubectl
docker build -t jenkins-docker -f Dockerfile.jenkins .

# Run Jenkins container
docker run -d \
  --network host \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $HOME/.kube:/var/jenkins_home/.kube:ro \
  -v $HOME/.minikube:/home/sakshi/.minikube:ro \
  --name jenkins \
  --group-add $(getent group docker | cut -d: -f3) \
  jenkins-docker
```

### 2. Configure Jenkins Pipeline
1. Access Jenkins UI at http://localhost:8080
2. Install suggested plugins
3. Create new Pipeline job
4. Configure GitHub repository
5. Use the provided Jenkinsfile for pipeline definition

### 3. Pipeline Stages
- **Build**: Creates Docker image
- **Test**: Runs application tests
- **Deploy**: Deploys to Kubernetes cluster

## Project Structure
```
todo-app/
├── app/
│   └── app.py              # Flask application
├── kubernetes/
│   ├── deployment.yaml     # Kubernetes deployment
│   └── service.yaml        # Kubernetes service
├── Dockerfile             # Application Dockerfile
├── Dockerfile.jenkins     # Jenkins Dockerfile
├── jenkins-job-config.xml # Jenkins job configuration
├── requirements.txt       # Python dependencies
└── README.md
```

## Troubleshooting

### Jenkins-Kubernetes Integration
If kubectl commands fail in Jenkins:
```bash
# Verify kubectl access
docker exec jenkins kubectl --kubeconfig=/var/jenkins_home/.kube/config get nodes

# Check Minikube status
minikube status
```

### Common Issues
1. **Jenkins Docker Access**
   - Verify docker.sock mount
   - Check Jenkins user in docker group

2. **Kubernetes Authentication**
   - Verify kubeconfig mounting
   - Check certificate paths
   - Ensure host network access

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License
MIT License
