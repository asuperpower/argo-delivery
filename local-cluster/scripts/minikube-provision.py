#!/usr/bin/env python3

import subprocess
def minikube_instance_exists(environment):
    """
    Check if a Minikube instance for the given environment already exists.
    """
    cmd = f"minikube status -p k8s-{environment} --format='{{{{.Host}}}}'"
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip() == "Running"
    except subprocess.CalledProcessError:
        return False

def create_minikube_instance(environment):
    """
    Creates a Minikube instance for the given environment using a formatted command string.
    """
    cmd = f"minikube start --memory 2000 --cpus 2 --disk-size 3GB -p k8s-{environment}"

    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to create Minikube instance for {environment} environment: {e}")

def bootstrap_argocd(environment):
    """
    Bootstraps ArgoCD onto the Minikube cluster for the given environment.
    """
    crds_path = "local-cluster/argocd-bootstrap/overlays/crds"
    env_path = f"local-cluster/argocd-bootstrap/overlays/{environment}"
    
    # Install the CRDs first
    crds_cmd = f"kustomize build {crds_path} | kubectl --context k8s-{environment} apply -f -"
    try:
        subprocess.run(crds_cmd, shell=True, check=True)
        print(f"Successfully installed ArgoCD CRDs for {environment} environment")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install ArgoCD CRDs for {environment} environment: {e}")
        return

    # Install the rest of ArgoCD
    env_cmd = f"kustomize build --enable-helm {env_path} | kubectl --context k8s-{environment} apply -f -"
    try:
        subprocess.run(env_cmd, shell=True, check=True)
        print(f"Successfully bootstrapped ArgoCD for {environment} environment")
    except subprocess.CalledProcessError as e:
        print(f"Failed to bootstrap ArgoCD for {environment} environment: {e}")

def main():
    environments = ['dev', 'int', 'prod']
    for env in environments:
        # if not minikube_instance_exists(env):
        create_minikube_instance(env)
        bootstrap_argocd(env)

if __name__ == "__main__":
    main()
