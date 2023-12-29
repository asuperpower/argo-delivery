import subprocess

def stop_minikube_instance(environment):
    """
    Stop a Minikube instance for the given environment using a formatted command string.
    """
    stop_cmd = f"minikube stop -p k8s-{environment}"
    delete_cmd = f"minikube delete -p k8s-{environment}"

    try:
        subprocess.run(stop_cmd, shell=True, check=True)
        subprocess.run(delete_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to create Minikube instance for {environment} environment: {e}")

def main():
    environments = ['dev', 'int', 'prod']
    for env in environments:
        stop_minikube_instance(env)

if __name__ == "__main__":
    main()
