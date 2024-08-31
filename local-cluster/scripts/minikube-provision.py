#!/usr/bin/env python3

import subprocess

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
    cmd = f"kubectl --context k8s-{environment} apply -k ../argocd-bootstrap/overlays/{environment}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Successfully bootstrapped ArgoCD for {environment} environment")
    except subprocess.CalledProcessError as e:
        print(f"Failed to bootstrap ArgoCD for {environment} environment: {e}")

def main():
    environments = ['dev', 'int', 'prod']
    for env in environments:
        create_minikube_instance(env)
        bootstrap_argocd(env)

if __name__ == "__main__":
    main()
