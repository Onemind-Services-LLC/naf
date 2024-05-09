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

- now if u are in container exit from container using below command
![alt text](image-4.png)
- now lets create a folder with name `git_python_automation` in user's home directory using below commands
```sh
cd ~
mkdir git_python_automation
cd git_python_automation
```
![alt text](image-5.png)

- open the vscode in `git_python_automation` using below command
```sh
code .
```
![alt text](image-6.png)
- now you can see vscode opened in `git_python_automation` directory
![alt text](image-7.png)

- lets create a new file with name `restore_config.py`
![alt text](image-8.png)
- paste the below content in it.
```python
from netmiko import ConnectHandler
import subprocess
# Prompt the user to enter router details
host = input("Enter router IP address: ")
username = input("Enter username: ")
password = input("Enter password: ")
enable_secret = input("Enter enable secret (if any): ")

# Router details
router_details = {
    'device_type': 'cisco_xe',
    'host': host,
    'username': username,
    'password': password,
    'secret': enable_secret  # Assuming this is the enable secret
}

# Prompt the user to enter GitLab access token
gitlab_access_token = input("Enter GitLab access token: ")
gitlab_repo_url = f'http://auth2:{gitlab_access_token}@172.16.14.101/ansible/router_configurations.git'

# Clone the GitLab repository
clone_command = f'git clone {gitlab_repo_url}'
subprocess.run(clone_command, shell=True, check=True)

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
    # Check interface configuration after changes
    print("Interface configuration after changes:")
    print(ssh.send_command("sh run int gig4"))

print("Router configuration has been updated.")
```
![alt text](image-9.png)
make sure you should put the proper gitlab repository url.
## Explanation:

  - The script uses the netmiko library to connect to a Cisco XE router and execute commands.
  - It defines connection details for the router (csr1000v dictionary), including IP address, credentials, and SSH port.
  - The run_commands_on_router function establishes an SSH connection to the router and executes specified commands. It returns the output of the commands.
  - In the main block (if __name__ == "__main__":), it specifies the commands to run on the router (commands_to_run), which includes "sh run int gig4" to show the configuration of interface GigabitEthernet4.
  - It executes the commands using the run_commands_on_router function and prints the output.


To run the program in a Docker container, follow these steps:

1. Open the terminal.

![alt text](image-10.png)

2. Run the container with the appropriate bind mount using the following command:

```sh
docker container run -it -v $(pwd):/git_python_automation ansible_lab
```
3. Navigate to the `/python_automation` directory within the container:
```sh
cd /python_automation
```
![alt text](image-11.png)
4. Run the Python program:

```sh
python restore_config.py
```

![alt text](image-12.png)

This will execute the `restore_config.py` program within the Docker container, allowing you to check the status of the device.

#### Note: When prompted, ensure to pass the GitLab access token for authentication.

## Conclusion:

This lab exercise provides a practical guide for managing router configurations using GitLab and Python scripts, facilitating automation and version control in network management tasks.
