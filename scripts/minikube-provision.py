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

def main():
    environments = ['dev', 'int', 'prod']
    for env in environments:
        create_minikube_instance(env)

if __name__ == "__main__":
    main()
