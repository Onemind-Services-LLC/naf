from netmiko import ConnectHandler
import subprocess

# Router details
router_details = {
    'device_type': 'cisco_xe',
    'host':   '172.16.14.110',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'  # Assuming this is the enable secret
}

# Prompt the user to enter GitLab access token
gitlab_access_token = input("Enter GitLab access token: ")
gitlab_repo_url = f'http://auth2:{gitlab_access_token}@172.16.14.101/ansible/router_configurations.git'

# Clone the GitLab repository
clone_command = f'git clone {gitlab_repo_url}'
# subprocess.run(clone_command, shell=True, check=True)

# Path to the configuration file within the cloned repository
config_file_path = './router_configurations/routerconf.txt'

# Read configurations from file
with open(config_file_path, "r") as file:
    router_config = file.readlines()

# Connect to router
with ConnectHandler(**router_details) as ssh:
    ssh.enable()  # Enter enable mode

    # Configure router
    ssh.send_config_set(router_config)

    # Optionally, you can save the configuration
    ssh.save_config()
