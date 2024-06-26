##  Exercise: Manage Router Configurations using Python and Gitlab
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
- Click on the plus icon in the top menu.
![alt text](./images/image.png)
- Click on new project
![alt text](./images/image-1.png)
- Click on *create blank project*
- Go to GitLab and create a new project/repository named `router_configurations`.
![alt text](./images/image-2.png)
- Ensure "Initialize repository with a README" is selected.
- Click "Create project".

### 2. Add Configuration to the Repository:

- Inside the repository, create a new file named `routerconf.txt`.
- Click add new file
 
  ![alt text](./images/image-3.png)
  
- Add the following content to the file:

```
interface loopback100
  ip address 100.100.100.100 255.255.255.0
```
![alt text](./images/image-64.png)

### 3. Create an Access Token:

- Go to the project's settings and click on "Access Tokens".
- Give a name to the token "access-token-for-python" and generate a new access token.

![alt text](./images/d9ded552-6e91-4728-a52d-3e9b974c2645.png)

- Copy the access token.

![alt text](./images/a7899266-15d2-4bb1-b856-7cea00faf978.png)

- If you're logged into a container, exit from the container using the following command.

  ![alt text](./images/image-4.png)
  
- Let's create a folder named git_python_automation in the user's home directory using the commands below.
  
   ```sh
   cd ~
   mkdir git_python_automation
   cd git_python_automation
   ```
   ![alt text](./images/image-5.png)

- Open Visual Studio Code in the git_python_automation folder using the command below.
   ```sh
   code .
   ```
   ![alt text](./images/image-6.png)

- Visual Studio Code is now open in the git_python_automation directory.
   ![alt text](./images/image-7.png)

- Lets create a new file with name `restore_config.py`
  ![alt text](./images/image-8.png)

- Paste the following content into the Python file.
```python
from netmiko import ConnectHandler
import subprocess

# Router details
router_details = {
    'device_type': 'cisco_nxos',
    'host': '172.16.14.210',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'  # Assuming this is the enable secret
}

# Prompt the user to enter GitLab access token
gitlab_access_token = input("Enter GitLab access token: ")
gitlab_repo_url = f'http://auth2:{gitlab_access_token}@172.16.14.202/ansible/router_configurations.git'

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
    print(ssh.send_command("sh run int lo100"))

print("Router configuration has been updated.")
```
  

   Ensure that you put the correct GitLab repository URL.

  ## Script Explanation:

   - The script uses the netmiko library to connect to a Cisco XE router and execute commands.
   - It defines connection details for the router (csr1000v dictionary), including IP address, credentials, and SSH port.
   - The run_commands_on_router function establishes an SSH connection to the router and executes specified commands. It returns the output of the commands.
   - In the main block (if __name__ == "__main__":), it specifies the commands to run on the router (commands_to_run), which includes "sh run int gig4" to show the configuration of interface GigabitEthernet4.
   - It executes the commands using the run_commands_on_router function and prints the output.


## To run the program in a Docker container, follow these steps:

  -  Open the terminal.

     ![alt text](./images/image-10.png)

  -  Run the container with the appropriate bind mount using the following command:

      ```sh
      docker container run -it -v $(pwd):/git_python_automation ansible_lab
      ```
      If you encounter issues while creating the Docker image, replace the image name with the one we have already pushed to Docker registry. Use the image name onemindservices2024/naf2024 instead of ansible_lab. The new command will look like this:
 
      ```sh
         docker container run -it -v $(pwd):/git_python_automation onemindservices2024/naf2024
      ```

   - Navigate to the `/git_python_automation` directory within the container:
      ```sh
      cd /git_python_automation
      ```
   
   - Run the Python program:
   
      ```sh
      python restore_config.py
      ```
   
   
      This will execute the `restore_config.py` program within the Docker container, allowing you to check the status of the device.

   ![alt text](./images/image-65.png)
   
   #### Note: When prompted, ensure to pass the GitLab access token for authentication.

## Conclusion:

This lab exercise provides a practical guide for managing router configurations using GitLab and Python scripts, facilitating automation and version control in network management tasks.
