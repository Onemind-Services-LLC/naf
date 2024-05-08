# Exercise-4: Managing Router Configurations with GitLab and Python

## Objective:
In this lab, you will learn how to manage router configurations using GitLab for version control and Python scripts for automation.

## Steps:

### 1. Create a New GitLab Project:

- Go to GitLab and create a new project/repository named `router_configurations`.
- Ensure "Initialize repository with a README" is selected.
- Click "Create project".

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/f59bf45e-ed1e-4a35-aa46-01827c9a071a)


### 2. Add Configuration to the Repository:

- Inside the repository, create a new file named `routerconf.txt`.
- Add the following content to the file:

```
interface GigabitEthernet4
ip address 1.1.1.1 255.255.255.0
no shutdown
```
  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/4efebc68-3c66-4b4f-b9da-0ce86f0e6903)


### 3. Create an Access Token:

- Go to the project's settings and click on "Access Tokens".
- Give a name to the token (e.g., `access-token-for-python`) and generate a new access token.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/d9ded552-6e91-4728-a52d-3e9b974c2645)

- Copy the access token.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/a7899266-15d2-4bb1-b856-7cea00faf978)


### 4. Manage Router Configurations:

Log in to the interface server via SSH and execute the following command

```bash
ssh 172.16.14.10 -l admin
sh run int gig4
```
![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/2cd88f8e-8581-46fe-b9a1-e95049167e1c)

Note that the current IP address is 5.5.5.5 from the interface configuration

#### 4.1. restore_config.py:

```python
from netmiko import ConnectHandler

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

# Path to the configuration file within the cloned repository
config_file_path = './router_configurations/routerconf.txt'

# Read configurations from file
with open(config_file_path, "r") as file:
    router_config = file.readlines()

# Connect to router
with ConnectHandler(**router_details) as ssh:
    ssh.enable()  # Enter enable mode

    # Check interface configuration before making changes
    print("Interface configuration before changes:")
    print(ssh.send_command("sh run int gig4"))

    # Configure router
    ssh.send_config_set(router_config)

    # Optionally, you can save the configuration
    ssh.save_config()

    # Check interface configuration after changes
    print("Interface configuration after changes:")
    print(ssh.send_command("sh run int gig4"))

print("Router configuration has been updated.")
```

## Explanation:

  - The script uses the netmiko library to connect to a Cisco XE router and execute commands.
  - It defines connection details for the router (csr1000v dictionary), including IP address, credentials, and SSH port.
  - The run_commands_on_router function establishes an SSH connection to the router and executes specified commands. It returns the output of the commands.
  - In the main block (if __name__ == "__main__":), it specifies the commands to run on the router (commands_to_run), which includes "sh run int gig4" to show the configuration of interface GigabitEthernet4.
  - It executes the commands using the run_commands_on_router function and prints the output.

## Note: When prompted, ensure to pass the GitLab access token for authentication.

Ensure you have Python installed on your system. Check using python --version.

Run check_interface.py script using the following command:

```bash
python restore_config.py
```

![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/04fed1fb-5561-4eea-9e2b-a5363c8e6248)

Log in to the interface server again via SSH and compare the interface configuration before and after running the script to verify the changes.
The ip configuration is now changed to 1.1.1.1 from 5.5.5.5

![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/b0a43161-e4c8-4a08-b824-7ebee0cc43dd)


#### 4.2. Verify Interface Status Using Python:

Alternatively execute the check_interface.py script to verify the configuration change by running `check_interface.py` script using the command `python3 check_interface.py`.

## check_interface.py:

```python
from netmiko import ConnectHandler

csr1000v = {
    'device_type': 'cisco_xe',
    'host': '172.16.14.110',
    'username': 'admin',
    'password': 'admin',
    'port': 22,
    'secret': 'admin'
}

def run_commands_on_router(device_info, commands):
    try:
        with ConnectHandler(**device_info) as ssh:
            ssh.enable()  # Enter privileged mode
            output = ""
            for command in commands:
                output += ssh.send_command(command) + "\n"
            return output
    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == "__main__":
    commands_to_run = [
        "sh run int gig4"  # Add more commands as needed
    ]
    router_output = run_commands_on_router(csr1000v, commands_to_run)
    if router_output:
        print("Router Output:")
        print(router_output)
    else:
        print("Failed to retrieve router output.")
```

![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/a1bfd081-8871-435f-9698-8610ccc36065)


## Conclusion:

This lab exercise provides a practical guide for managing router configurations using GitLab and Python scripts, facilitating automation and version control in network management tasks.
