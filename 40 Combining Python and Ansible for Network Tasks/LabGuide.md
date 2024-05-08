# Overview

Ansible dynamic inventories are a feature that allows Ansible to fetch host information from external sources dynamically rather than using static inventory files. This approach enables Ansible to adapt to dynamic or cloud-based environments where hosts may be frequently added, removed, or modified. Dynamic inventories are particularly useful in scenarios such as auto-scaling environments, cloud infrastructure, and large-scale deployments where maintaining a static inventory file becomes impractical.

Here's an overview of how Ansible dynamic inventories work and how they can be leveraged:

### 1. Data Sources:
Dynamic inventories can fetch host information from various data sources, including:

- Cloud providers such as AWS, Azure, Google Cloud, and OpenStack.
- Configuration management databases (CMDBs) like ServiceNow or PuppetDB.
- External APIs, databases, or other systems that store host information.

### 2. Supported Formats:
Ansible dynamic inventories support multiple formats for representing host information, including JSON, YAML, and INI. The inventory data fetched from the external source must be formatted according to one of these supported formats for Ansible to interpret it correctly.

### 3. Inventory Scripts:
To use dynamic inventories, you need to create executable inventory scripts written in Python. These scripts fetch host information from the external data source and format it according to one of the supported formats. The script then outputs the inventory data to stdout, which Ansible consumes during playbook execution.

### 4. Script Execution:
During playbook execution, Ansible runs the dynamic inventory script to fetch the inventory data dynamically. Ansible parses the output of the script to determine the hosts and groups available for targeting in the playbook. This allows Ansible to provision, configure, and manage hosts based on the dynamically fetched inventory data.

### 5. Configuration:
To use dynamic inventories with Ansible, you need to specify the path to the inventory script in your Ansible configuration file (ansible.cfg). You can also specify additional configuration options such as group mappings, host variables, and caching settings to optimize dynamic inventory performance.

### 6. Examples:
- AWS Dynamic Inventory: An inventory script can use the Boto3 library to fetch EC2 instance information from AWS and format it as JSON or YAML for Ansible consumption.
- OpenStack Dynamic Inventory: An inventory script can query the OpenStack API to retrieve information about VM instances and networks, then format it as JSON or YAML for Ansible.
- Custom Inventory Source: An organization may have a custom CMDB or database that stores host information. An inventory script can query this source, format the data, and output it as JSON or YAML for Ansible.

### 7. Benefits:

- Flexibility: Dynamic inventories adapt to changes in the infrastructure automatically, reducing manual maintenance overhead.
- Scalability: Dynamic inventories scale seamlessly to large environments with thousands of hosts or instances.
- Automation: Dynamic inventories enable automation of provisioning and management tasks, improving efficiency and reducing human error.


# Dynamic Plugin Inventory Example


# Custom Python Modules For Ansible

Custom Python modules in Ansible are Python scripts or libraries created by users to extend Ansible's functionality beyond what is provided by built-in modules.

Here are some key points about custom Python modules in Ansible:

- ### Purpose:
Custom Python modules are created to address specific use cases or requirements that cannot be fulfilled by Ansible's built-in modules alone. They allow users to integrate Ansible with external APIs, databases, or services, automate custom workflows, or perform tasks unique to their environment.
- ### Functionality: 
Custom Python modules can perform a wide range of tasks, including executing commands on remote hosts, querying databases, interacting with cloud providers' APIs, parsing data, generating reports, and more. The functionality of custom modules is limited only by what can be achieved with Python programming.  
- ### Structure:
Custom Python modules are Python scripts or libraries that follow a specific structure and naming convention to be recognized and executed by Ansible. They typically include functions or classes that implement the desired functionality and adhere to Ansible's module development guidelines.
- ### Usage:
Once created, custom Python modules can be used in Ansible playbooks just like built-in modules. Users can import and invoke custom modules within tasks to perform the desired actions on managed hosts or external systems.
- ### Distribution:
Custom Python modules can be distributed and shared with others through various channels such as version control repositories, Ansible Galaxy, or custom package repositories. Sharing custom modules allows users to benefit from each other's contributions and avoid reinventing the wheel.
- ### Documentation:
It's essential to provide documentation and usage examples for custom Python modules to help users understand their purpose, functionality, and how to use them effectively in Ansible playbooks.

## Examples of Custom Python Modules For Ansible

Let's create a simple custom Python module for Ansible that generates a random password of a specified length. This module will allow us to generate random passwords dynamically during playbook execution.

Here's the structure of our custom Python module:

- Module Name: random_password.py
- Functionality: Generate a random password of a specified length.
- Input Parameters:
- 1. length: Length of the password to generate.
- 2. Output: Randomly generated password.

```python
#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    module = AnsibleModule(
        argument_spec=dict(
            length=dict(type='int', required=True)
        )
    )

    length = module.params['length']
    password = generate_password(length)

    module.exit_json(changed=False, password=password)

if __name__ == '__main__':
    main()

```

### Explanation of the code:

- We import AnsibleModule from ansible.module_utils.basic to create an Ansible module.  
- We define a function generate_password that takes a length parameter and generates a random password of the specified length using uppercase letters, lowercase letters, digits, and punctuation characters.  
- In the main function, we define the input parameters for our module (length) and use the generate_password function to generate a random password.  
-  Finally, we use module.exit_json to exit the module execution and return the generated password as the result.  
- To use this custom Python module in an Ansible playbook, you would save the code above to a file named random_password.py in the library directory of your Ansible project.  
- Then, you can invoke the module in your playbook like this:

```yaml
---
- hosts: localhost
  tasks:
    - name: Generate Random Password
      random_password:
        length: 12
      register: password_result

    - debug:
        msg: "Generated Password: {{ password_result.password }}"
```


## Another Example of Custom Python Modules For Network Automation

Let's create a custom Python module for Ansible that interacts with network devices to retrieve interface information. This module will use the Netmiko library, which provides a simple framework for executing commands on network devices via SSH.

Here's the structure of our custom Python module:

- Module Name: network_interface_info.py
- Functionality: Retrieve information about interfaces on network devices.
- Input Parameters:
- 1. host: Hostname or IP address of the network device.
- 2. username: Username for SSH authentication.
- 3. password: Password for SSH authentication.
- 4. Output: Dictionary containing interface information.

Below is the implementation of the custom Python module:

```python
#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from netmiko import ConnectHandler

def get_interface_info(host, username, password):
    """Retrieve information about interfaces on the network device."""
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }

    try:
        # Connect to the network device
        net_connect = ConnectHandler(**device)

        # Send command to retrieve interface information
        output = net_connect.send_command('show ip interface brief')

        # Parse interface information
        interface_info = {}
        for line in output.splitlines()[1:]:
            parts = line.split()
            if len(parts) >= 6:
                interface = parts[0]
                ip_address = parts[1]
                status = parts[4]
                protocol = parts[5]
                interface_info[interface] = {
                    'ip_address': ip_address,
                    'status': status,
                    'protocol': protocol
                }

        return interface_info

    except Exception as e:
        return {'error': str(e)}

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type='str', required=True),
            username=dict(type='str', required=True),
            password=dict(type='str', required=True, no_log=True)
        )
    )

    host = module.params['host']
    username = module.params['username']
    password = module.params['password']

    interface_info = get_interface_info(host, username, password)

    if 'error' in interface_info:
        module.fail_json(msg=interface_info['error'])
    else:
        module.exit_json(changed=False, interface_info=interface_info)

if __name__ == '__main__':
    main()

```

### Explanation of the code:

- We import AnsibleModule from ansible.module_utils.basic to create an Ansible module.
- We import ConnectHandler from netmiko to establish an SSH connection to network devices.
- We define a function get_interface_info that takes host, username, and password parameters and retrieves information about interfaces on the network device using the show ip interface brief command.
- In the main function, we define the input parameters for our module (host, username, password) and use the get_interface_info function to retrieve interface information.
- Finally, we use module.exit_json to exit the module execution and return the interface information as the result.
- To use this custom Python module in an Ansible playbook, you would save the code above to a file named network_interface_info.py in the library directory of your Ansible project. Then, you can invoke the module in your playbook like this:

```yaml
---
- hosts: network_devices
  tasks:
    - name: Retrieve Interface Information
      network_interface_info:
        host: "{{ ansible_host }}"
        username: "{{ ansible_user }}"
        password: "{{ ansible_password }}"
      register: interface_info

    - debug:
        var: interface_info
```


# Custom Filter Plugins For Ansible

Ansible custom filter plugins are Python scripts or functions that extend Ansible's built-in filters. Filters in Ansible are used to modify data or perform transformations on variables during playbook execution. Custom filter plugins allow users to create their own filters to meet specific requirements or perform custom transformations that are not available in Ansible's standard filter set.

Here are some key points about Ansible custom filter plugins:

- ### Purpose:
Custom filter plugins enable users to extend Ansible's filtering capabilities beyond the built-in filters provided by Ansible. They allow users to implement custom logic or transformations on data within Ansible playbooks.
- ### Functionality:
Custom filter plugins are implemented as Python functions or classes that accept input data and return transformed data. They can perform a wide range of operations, including string manipulation, data formatting, mathematical calculations, and more.
- ### Input Parameters:
Custom filter plugins can accept one or more input parameters, which are passed to the filter when it is invoked in a playbook. These parameters can be used to customize the behavior of the filter or provide input data for processing.
- ### Output:
Custom filter plugins return transformed data, which can be used in subsequent tasks or templates within the playbook. The output data may be of the same type as the input data or may be converted to a different type depending on the requirements of the filter.
- ### Usage:
Once created, custom filter plugins can be used in Ansible playbooks just like built-in filters. Users can invoke custom filters on variables or data structures within tasks, templates, or Jinja2 expressions to apply custom transformations.
- ### Distribution:
Custom filter plugins can be distributed and shared with others through various channels such as version control repositories, Ansible Galaxy, or custom package repositories. Sharing custom filters allows users to benefit from each other's contributions and leverage existing solutions to common problems.
- ### Documentation:
It's essential to provide documentation and usage examples for custom filter plugins to help users understand their purpose, functionality, and how to use them effectively in Ansible playbooks. Well-documented plugins contribute to better usability and adoption among the Ansible community.

## Examples of Custom Filter Plulgins For Ansible

Let's create a simple custom filter plugin in Ansible that converts a string to title case, where the first letter of each word is capitalized. We'll name our filter plugin titlecase.

Here's how you can create the custom filter plugin:

- Create a directory named filter_plugins in your Ansible project directory.
- Inside the filter_plugins directory, create a Python file named titlecase.py.
- Add the following code to titlecase.py:

```python
class FilterModule(object):
    """Custom filters."""

    def filters(self):
        return {
            'titlecase': self.titlecase_filter
        }

    def titlecase_filter(self, value):
        """Convert a string to title case."""
        return ' '.join(word.capitalize() for word in value.split())

```
### Explanation of the code:

- We define a class named FilterModule, which serves as our custom filter plugin.
Inside the class, we define a method named filters, which returns a dictionary mapping filter names to filter functions.  
- In this case, we define a filter named titlecase, which is mapped to the titlecase_filter method.
The titlecase_filter method takes a string as input, splits it into words, capitalizes the first letter of each word, and joins them back together with spaces.  
- This filter converts a string to title case.  
- Now that we've created our custom filter plugin, let's see how to use it in an Ansible playbook:  

```yaml
---
- hosts: localhost
  vars:
    my_string: "hello world"

  tasks:
    - name: Apply title case filter
      debug:
        msg: "{{ my_string | titlecase }}"
```

## Another Example of Custom Filter Plulgins For Network Automation

Let's create a custom filter plugin for a network automation use case. In this example, we'll create a filter plugin that formats a MAC address in a standardized format.

Here's how you can create the custom filter plugin:

- Create a directory named filter_plugins in your Ansible project directory.  
- Inside the filter_plugins directory, create a Python file named mac_format.py.  
- Add the following code to mac_format.py:  

```python
class FilterModule(object):
    """Custom filters for network automation."""

    def filters(self):
        return {
            'format_mac': self.format_mac_filter
        }

    def format_mac_filter(self, value):
        """Format a MAC address in a standardized format."""
        value = value.lower().replace('-', ':')  # Convert to lowercase and replace dashes with colons
        parts = [value[i:i+2] for i in range(0, len(value), 2)]  # Split into pairs of characters
        formatted_mac = ':'.join(parts)  # Join pairs with colons
        return formatted_mac

```

### Explanation of the code:

- We define a class named FilterModule, which serves as our custom filter plugin.
Inside the class, we define a method named filters, which returns a dictionary mapping filter names to filter functions.
- In this case, we define a filter named format_mac, which is mapped to the format_mac_filter method.
- The format_mac_filter method takes a MAC address string as input, converts it to lowercase, replaces dashes with colons, splits it into pairs of characters, and joins them back together with colons.
- This filter formats a MAC address in a standardized format.

Now that we've created our custom filter plugin, let's see how to use it in an Ansible playbook

```yaml
---
- hosts: localhost
  vars:
    mac_address: "00-11-22-33-44-55"

  tasks:
    - name: Apply MAC address formatting filter
      debug:
        msg: "{{ mac_address | format_mac }}"

```

