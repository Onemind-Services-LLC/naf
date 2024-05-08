# Overview:

This documentation serves as an introduction to Ansible, a powerful automation tool, and its application in network automation. Ansible simplifies the management of network infrastructure by automating tasks such as configuration management, provisioning, and orchestration. This guide will explain the basics of Ansible and highlight its benefits in managing network infrastructure efficiently.  

# What is Ansible?
Ansible is an open-source automation tool that simplifies IT automation tasks, including configuration management, application deployment, and task orchestration. Developed by Red Hat, Ansible uses a simple and human-readable syntax (YAML) to define automation tasks, making it easy to learn and use.

# Role of Ansible in Network Automation:
In the context of network automation, Ansible allows network engineers and administrators to automate repetitive tasks across their network infrastructure. These tasks may include:

### 1. Configuration Management:
Ansible enables the management and configuration of network devices such as routers, switches, and firewalls. It ensures consistency in device configurations and helps enforce compliance with network policies.

### 2. Provisioning:
Ansible streamlines the process of provisioning new network resources by automating tasks such as device initialization, VLAN configuration, and IP address allocation.

### 3. Orchestration:
Ansible orchestrates complex network operations by coordinating tasks across multiple devices and platforms. It facilitates the automation of workflows such as network upgrades, migrations, and disaster recovery.


# Benefits of Using Ansible for Network Automation:

### 1. Increased Efficiency:  
Ansible automates repetitive tasks, reducing the time and effort required to manage network infrastructure.

### 2. Consistency:  
Ansible ensures consistency in network configurations by applying standardized templates and playbooks across all devices. This reduces the risk of human error and improves the reliability of the network.

### 3. Scalability:  
Ansible scales easily to manage networks of any size, from small-scale deployments to large, complex infrastructures. Its agentless architecture allows it to manage thousands of devices simultaneously, making it suitable for enterprise environments.

### 4. Simplified Management:  
Ansible's simple and declarative syntax makes it easy to define automation tasks and workflows. Network engineers can express complex configurations and operations using plain text files, making automation accessible to users of all skill levels.


# Understanding Ansible Components  
We'll explore the key components of Ansible, an automation tool widely used for configuration management, provisioning, and orchestration. Understanding these components is essential for harnessing the full power of Ansible in your automation workflows. Let's delve into each component and its role in the Ansible ecosystem  

### 1. Control Node
1. The control node is the machine where Ansible is installed and from which automation tasks are executed.
2. It serves as the central hub for managing the entire Ansible infrastructure.
3. The control node stores inventory information, playbooks, and configuration files.

### 2. Managed Nodes

1. Managed nodes are the devices or systems that Ansible manages and automates.
2. These nodes can be servers, networking devices, or any other devices capable of running Ansible modules.
3. Ansible communicates with managed nodes over SSH (Linux/Unix) or WinRM (Windows).

### 3. Inventories

1. Inventories are lists of managed nodes that Ansible can target for automation tasks.
2. Inventories can be defined as static files or dynamic sources such as cloud providers or inventory management systems.
3. They allow for grouping of hosts based on attributes such as function, location, or environment.

### 4. Playbooks

1. Playbooks are YAML-formatted files that define automation tasks to be executed by Ansible.
2. A playbook consists of one or more plays, each of which defines a set of tasks to be performed on a specific group of hosts.
3. Playbooks describe the desired state of the system and the steps needed to achieve that state.

### 5. Modules

1. Modules are small, reusable units of code that Ansible executes on managed nodes to perform specific tasks.
2. Ansible ships with a wide range of built-in modules for common tasks such as file management, package installation, and service management.
3. Custom modules can also be developed to extend Ansible's capabilities to meet specific requirements.

### 6. Tasks

1. Tasks are individual units of work defined within a playbook.
2. Each task calls a module and specifies the desired state of the system.
3. Tasks are executed sequentially by Ansible, and the results are reported back to the control node.  

### 7. Handlers

1. Handlers are a way to trigger actions or tasks only when notified by other tasks.
2. They are typically used for actions that should be performed at the end of a playbook, after all tasks have been executed, or in response to specific events.
3. Handlers are particularly useful for tasks like restarting services or triggering other system actions that should only occur if specific changes have been made.

```yaml
---
- name: Configure Network Devices
  hosts: network_devices
  tasks:
    - name: Ensure configuration file is present
      template:
        src: network_config.j2
        dest: /etc/network_config.conf
      notify: restart network service

  handlers:
    - name: restart network service
      service:
        name: networkd
        state: restarted

```

In this example:

- We have a playbook named "Configure Network Devices" that applies to hosts defined in the "network_devices" group.
- The tasks section contains a task that ensures the configuration file (network_config.j2) is present on the network devices. This task notifies the handler named "restart network service" if changes are made during the template application.
- The handlers section contains a handler named "restart network service" that restarts the network service (networkd) on the network devices. This handler is triggered by the task when changes are made to the configuration file.  

# Setting Up Ansible for Network Automation
We'll cover the installation of Ansible and the configuration steps required to work with network devices, including setting up the inventory file. By the end of this presentation, beginners will have a solid foundation for using Ansible to automate tasks across their network infrastructure.

### Installing Ansible:

##### Official Documentation  
https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html

Ansible can be installed on various operating systems, including Linux distributions such as Ubuntu, CentOS, and Red Hat Enterprise Linux.

1. On Ubuntu, you can install Ansible using the apt package manager:

```
sudo apt update
sudo apt install ansible
```

Once installed, verify the installation by running:
```
ansible --version
```

### Configuring Ansible:

The next step is to configure Ansible to work with your network devices. The primary configuration file for Ansible is located at /etc/ansible/ansible.cfg.  
Open the Ansible configuration file in a text editor such as nano or vim:
```
sudo nano /etc/ansible/ansible.cfg
```
Review the configuration options and adjust them according to your requirements. Common settings to consider include:  
1. inventory - Specifies the location of the inventory file.
2. remote_user - Specifies the default user to use for SSH connections to managed nodes.
3. private_key_file - Specifies the default SSH private key to use for authentication.
Save the changes and exit the text editor.


### Setting Up the Inventory File:

The inventory file is where you define your network devices and group them for management by Ansible.  
By default, the inventory file is located at /etc/ansible/hosts.  
Open the inventory file in a text editor:  
```
sudo nano /etc/ansible/hosts
```
Define your network devices in the inventory file using their IP addresses or hostnames. You can also group devices based on attributes such as location, function, or environment.  

Example inventory file:
```
[routers]
router1 ansible_host=192.168.1.1
router2 ansible_host=192.168.1.2
```
```
[switches]
switch1 ansible_host=192.168.1.3
switch2 ansible_host=192.168.1.4
```
Save the changes and exit the text editor.  

# Introduction to Basic Ansible Commands
In this section, we'll introduce you to some basic Ansible commands that are essential for getting started with network automation. These commands will help you interact with your network devices, gather information, and execute automation tasks efficiently using Ansible. Let's dive into each command and its usage.  

### 1. Ansible:

The ansible command is used to run ad-hoc commands against your managed nodes.  
Syntax: ansible [options] <host-pattern> [-m module_name] [-a 'module_arguments']  
Example: To gather information about the network devices and display their version, you can use the following command:  
```
ansible all -m raw -a 'show version'
```
This command sends the show version command to all hosts in your inventory.

### 2. Ansible-playbook:

The ansible-playbook command is used to execute playbooks, which are YAML-formatted files containing automation tasks.  
Syntax: ansible-playbook [options] playbook.yml  
Example: Suppose you have a playbook named configure_network.yml that configures interfaces on your network devices. You can run the playbook using the following command:  
```
ansible-playbook configure_network.yml
```
This command executes the tasks defined in the configure_network.yml playbook on the hosts specified in the playbook.

### 3. Ansible-doc:

The ansible-doc command is used to view documentation for Ansible modules.  
Syntax: ansible-doc <module_name>  
Example: If you want to learn more about the ios_config module, which is used for configuring Cisco IOS devices, you can use the following command:  
```
ansible-doc ios_config
```
This command displays detailed documentation for the ios_config module, including usage examples and available options.

# Sample Playbooks for Network Automation
We'll explore sample playbooks that demonstrate common network automation tasks using Ansible. These playbooks are designed to help beginners understand the structure and syntax of Ansible playbooks while showcasing practical examples of network automation. By studying these playbooks, you'll gain insights into how Ansible can be used to automate tasks across your network infrastructure.  

### 1. Configure Interfaces Playbook:

- Purpose: This playbook automates the configuration of interfaces on network devices, such as routers and switches.
- Tasks:
Set interface descriptions to provide meaningful labels for each interface.  
Assign IP addresses to interfaces to enable network connectivity.  
Configure VLANs to segment network traffic effectively.  
- Modules Used:  
ios_config (for Cisco IOS devices) or nxos_config (for Cisco Nexus devices) to send configuration commands to network devices.  

```yaml
---
- name: Configure Interfaces
  hosts: network_devices
  tasks:
    - name: Set interface descriptions
      ios_config:
        lines:
          - interface GigabitEthernet1/0/1
          - description Connected to Server
      provider: "{{ ansible_network_os }}"
    
    - name: Assign IP addresses to interfaces
      ios_config:
        lines:
          - interface GigabitEthernet1/0/1
          - ip address 192.168.1.1 255.255.255.0
      provider: "{{ ansible_network_os }}"
    
    - name: Configure VLANs
      ios_config:
        lines:
          - vlan 100
          - name Sales
      provider: "{{ ansible_network_os }}"
```

### 2. Update Firmware Playbook:

- Purpose: This playbook automates the process of updating firmware on network devices.
- Tasks:  
Download the latest firmware images from a central repository.  
Install the firmware updates on network devices.  
- Modules Used:  
ios_command or nxos_command to execute commands to download and install firmware updates.  

```yaml
---
- name: Update Firmware
  hosts: network_devices
  tasks:
    - name: Download firmware image
      ios_command:
        commands:
          - copy tftp://10.0.0.1/firmware.bin flash:
      provider: "{{ ansible_network_os }}"
    
    - name: Install firmware update
      ios_command:
        commands:
          - boot system flash:firmware.bin
      provider: "{{ ansible_network_os }}"
```

### 3. Deploy ACLs Playbook:

- Purpose: This playbook automates the deployment of access control lists (ACLs) to restrict traffic on network devices.  
- Tasks:  
Define access control rules to permit or deny specific types of traffic.  
Apply ACLs to interfaces to enforce security policies.  
- Modules Used:  
ios_acl or nxos_acl to configure access control lists on network devices.  

```yaml
---
- name: Deploy ACLs
  hosts: network_devices
  tasks:
    - name: Define ACL entry
      ios_acl:
        access_list: ACL_OUT
        access_list_type: extended
        rule: permit tcp any any eq 80
      provider: "{{ ansible_network_os }}"
    
    - name: Apply ACL to interface
      ios_config:
        lines:
          - interface GigabitEthernet1/0/1
          - ip access-group ACL_OUT out
      provider: "{{ ansible_network_os }}"
```  

# Troubleshooting and Debugging Ansible Playbooks
In this section, we'll explore techniques for troubleshooting and debugging Ansible playbooks. Troubleshooting is an essential skill for any Ansible user, as it helps identify and resolve issues that may arise during playbook execution. By understanding how to effectively troubleshoot and debug playbooks, you'll be better equipped to overcome challenges and ensure the success of your automation tasks.  

### 1. Increased Verbosity (-vvv):  
The -vvv option is used to increase the verbosity level of Ansible output, providing more detailed information about playbook execution.  
When troubleshooting, using increased verbosity can help you identify where a playbook is failing and pinpoint the cause of the issue.  
Example:
```
ansible-playbook playbook.yml -vvv
```

### 2. Dry Runs (--check):
The --check option is used to perform a dry run of a playbook without making any actual changes to the target system.  
This allows you to preview the changes that would be applied by the playbook without actually applying them, helping to prevent unintended consequences.  
Example:  
```
ansible-playbook playbook.yml --check
```

### 3. Interpreting Error Messages:

Error messages provide valuable information about what went wrong during playbook execution.  
Pay close attention to error messages, as they often contain clues about the root cause of the issue.  
Look for specific error codes, module names, and line numbers to help identify where the problem occurred.  
Example Error Message:  
```
ERROR! 'dict object' has no attribute 'missing_attribute'
```

### 4. Debugging Techniques:

Use the debug module to print debug messages during playbook execution.  
Place debug tasks strategically throughout your playbook to inspect variables, module outputs, and other relevant information.  
Example:  
```yaml
- name: Debug message
  debug:
    msg: "Variable value: {{ my_variable }}"
```

### 5. Reviewing Playbook Syntax:

Check your playbook syntax using the ansible-playbook command with the --syntax-check option.  
This will ensure that your playbook is correctly formatted and free of syntax errors before execution.  
Example:  
```
ansible-playbook playbook.yml --syntax-check
```

# Ansible Documentation and Learning Resources

### 1. Ansible Documentation:

The official Ansible documentation is a comprehensive resource that covers all aspects of Ansible, including installation, usage, modules, and best practices. The documentation is regularly updated and maintained by the Ansible community, ensuring accuracy and relevance.  

### 2. Ansible Galaxy:

Ansible Galaxy is a hub for finding, sharing, and collaborating on Ansible roles.  
Users can search for pre-built Ansible roles to automate common tasks and integrate them into their playbooks.  
Ansible Galaxy also provides documentation and examples for each role, making it easy to get started.

### 3. Tutorials and Guides:

There are many tutorials and guides available online that provide step-by-step instructions and hands-on exercises for learning Ansible.  
Websites like Ansible.com, YouTube, and tech blogs often publish tutorials covering various Ansible topics, from beginner to advanced.  
Encourage users to explore these tutorials to gain practical experience and insights into Ansible usage.  

### 4. Ansible Blogs and Articles:

Many Ansible experts and enthusiasts share their knowledge and experiences through blogs and articles.  
Reading blog posts and articles can provide valuable tips, best practices, and real-world use cases for using Ansible.  

### 5. Community Forums and Discussion Groups:

Community forums and discussion groups are great places to seek help, ask questions, and learn from other Ansible users.  
Websites like Stack Overflow, Reddit, and the Ansible Community Forum host active communities where users can interact and share knowledge.  
