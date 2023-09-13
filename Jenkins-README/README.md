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

...

4. **Expose Jenkins as a LoadBalancer:**
    ```bash
    kubectl expose deployment jenkins --type=LoadBalancer --name=jenkins-lb --port=8080
    ```

5. **Access Jenkins:**
    
    - Get the external IP address of the Jenkins LoadBalancer:
      ```bash
      kubectl get svc jenkins-lb
      ```

    - Once the `EXTERNAL-IP` is assigned, visit `http://[EXTERNAL-IP]:8080` in your browser.

...


6. **Complete the Jenkins Setup:**

    - Retrieve the Jenkins unlock key:
      ```bash
      kubectl get secret jenkins -o=jsonpath="{.data.jenkins-admin-password}" | base64 --decode
      ```

    - Install your desired plugins and finish the setup.

