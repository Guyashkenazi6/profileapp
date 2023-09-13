# Jenkins Installation on Google Cloud Kubernetes Cluster

## Prerequisites
- A running Google Cloud Kubernetes Cluster
- `kubectl` and `gcloud` command-line tools installed

## Installation Steps

1. **Set up Google Cloud SDK (if not already done):**
    ```bash
    gcloud init
    ```

2. **Connect to your Kubernetes Cluster:**
    ```bash
    gcloud container clusters get-credentials [CLUSTER_NAME] --zone [ZONE]
    ```

3. **Install Jenkins using Helm:**

    - First, add the Jenkins chart:
      ```bash
      helm repo add jenkins https://charts.jenkins.io
      helm repo update
      ```

    - Then, deploy Jenkins:
      ```bash
      helm install jenkins jenkins/jenkins
      ```

4. **Access Jenkins:**
    
    - Forward the Jenkins service port to your local machine:
      ```bash
      kubectl port-forward svc/jenkins 8080:8080
      ```

    - Visit [http://localhost:8080](http://localhost:8080) in your browser.

5. **Complete the Jenkins Setup:**

    - Retrieve the Jenkins unlock key:
      ```bash
      kubectl get secret jenkins -o=jsonpath="{.data.jenkins-admin-password}" | base64 --decode
      ```

    - Install your desired plugins and finish the setup.

