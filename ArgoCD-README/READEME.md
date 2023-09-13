# Installing ArgoCD on Google Kubernetes Engine via Helm

## Prerequisites

- A running GKE cluster.
- Helm installed and configured. [Installation Guide](https://helm.sh/docs/intro/install/)

## Steps

1. **Add the ArgoCD Helm repository:**
    ```bash
    helm repo add argo https://argoproj.github.io/argo-helm
    helm repo update
    ```

2. **Install ArgoCD:**
    ```bash
    helm install argocd argo/argo-cd
    ```

3. **Expose ArgoCD as a LoadBalancer:**
    Update the ArgoCD Helm release to expose the ArgoCD Server service as a LoadBalancer.
    ```bash
    helm upgrade argocd argo/argo-cd \
      --set server.service.type=LoadBalancer
    ```

4. **Access ArgoCD:**
    
    - Get the external IP address of the ArgoCD Server LoadBalancer:
      ```bash
      kubectl get svc argocd-argocd-server
      ```

      Wait for the `EXTERNAL-IP` to change from `<pending>` to an actual public IP address. This might take a few minutes.

    - Once the `EXTERNAL-IP` is assigned, visit `https://[EXTERNAL-IP]` in your browser.
      The default admin password is the name of the ArgoCD API server pod in the `argocd` namespace. Retrieve it with:
      ```bash
      kubectl get pods -n default -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2
      ```

## Security Note

Exposing services through a LoadBalancer can expose your applications to the wider internet. Ensure you have proper security, authentication mechanisms, and consider using network policies in place. Furthermore, when using a LoadBalancer in a cloud provider, you might incur additional costs.

