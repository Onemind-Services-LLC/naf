##  Exercise:
### Problem Statement:
1. **Create a Private Git Repository on GitLab**: Start by creating a private Git repository on GitLab where you'll store your router configurations. Ensure that the repository is private to restrict access.

2. **Add Router Configuration File**: Inside the private Git repository, add a file containing your router configurations.

3. **Python Program Input**: Develop a Python program that prompts the user to input the following information:
   - Username
   - IP address
   - Password
   - Port

4. **Use GitLab Access Token**: Ensure that your Python program uses a GitLab access token to access the private repository. This token will provide authentication and authorization to pull the router configurations.

5. **Pull and Apply Configurations**: Your Python program should then use the provided credentials and the GitLab access token to pull the router configurations from the private repository and apply them to the router.

By following these steps, you'll have a Python program that securely pulls router configurations from a private Git repository on GitLab and applies them to the router based on user input.

### Solution
## Steps:

### 1. Create a New GitLab Project:
- in the top menu click on plus icon
![alt text](image.png)
- click on new project
![alt text](image-1.png)
- click on *create blank project*
- Go to GitLab and create a new project/repository named `router_configurations`.
![alt text](image-2.png)
- Ensure "Initialize repository with a README" is selected.
- Click "Create project".

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/f59bf45e-ed1e-4a35-aa46-01827c9a071a)


### 2. Add Configuration to the Repository:

- Inside the repository, create a new file named `routerconf.txt`.
- Add the following content to the file:
![alt text](image-3.png)

```
interface Loopback0
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


Log in to the interface server via SSH and execute the following command

```bash
ssh 172.16.14.10 -l admin
sh run int gig4
```

![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/a1bfd081-8871-435f-9698-8610ccc36065)


## Conclusion:

This lab exercise provides a practical guide for managing router configurations using GitLab and Python scripts, facilitating automation and version control in network management tasks.
