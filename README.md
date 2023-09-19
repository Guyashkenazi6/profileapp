![plot](/images/profileapp.png)

# DevOps Engineer Final Project

Welcome to my final project as a DevOps Engineer. This project encapsulates the tools, methodologies, and practices that represent the cutting edge of DevOps. Designed meticulously with a myriad of modern tools, this repository showcases the capabilities of a well-integrated CI/CD pipeline, all orchestrated on the Google Cloud platform.

## 🚀 Features

- A Flask web application written in Python.
- Showcases links to LinkedIn, GitHub, and GitLab with corresponding logos.
- Links and logos are fetched from MongoDB, demonstrating a seamless integration of web frameworks with databases.
- CI/CD pipeline that involves Jenkins, ArgoCD, and Helm charts.
- Seamless containerization using Docker.
- Monitoring and logging capabilities using Grafana and Prometheus.

## 🛠️ Tech Stack

- **Orchestration**: Kubernetes
- **Containerization**: Docker
- **Cloud Platform**: Google Cloud
- **CI/CD**: Jenkins, ArgoCD, Helm
- **Database**: MongoDB
- **Programming**: Python, Flask
- **Monitoring**: Grafana, Prometheus

## 🌐 Web Application

The application provides three primary links:

1. LinkedIn
2. GitHub
3. GitLab

Each link is supplemented with an appropriate logo, fetched dynamically from MongoDB.

## 🔧 CI/CD Pipeline Overview

1. **Continuous Integration (CI)**: On every code commit:
    - Jenkins triggers the CI pipeline.
    - The Flask app is tested using pytest.
    - Upon successful tests, Docker creates a container image.
    - The newly built image is pushed to DockerHub.
  
2. **Continuous Deployment (CD)**:
    - Helm charts describe the desired deployment state.
    - ArgoCD takes care of deploying these Helm charts, ensuring the application is always running in the desired state on Kubernetes.

3. **Kubernetes on GCP**: The Kubernetes service on Google Cloud facilitates the deployment. Using a LoadBalancer, it provides an external IP, making the app accessible from the internet.

4. **Ingress**: Ingress services are set up for the main app, Argo, and Jenkins, streamlining network traffic and ensuring secured access.

## 🚀 Quick Start

*Coming Soon: Steps on how to run the project locally, access deployed versions, etc.*

## 🔗 Links & Resources

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [DockerHub Repository](https://hub.docker.com/repositories/guyashkenazi)
---

🌟 Star this repo if you found it useful! Feedback and PRs are welcomed.

