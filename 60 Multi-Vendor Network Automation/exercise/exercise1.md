# Multi-Vendor Network Automation: Configuring VLAN on different vendor switches

# Lab topology
* Below is the lab topology used for this configuration demonstration.


![alt text](image.png)

### Problem Statement:
* Configure VLANs on devices from different vendors.

### Solution:
* Develop a Python script to configure VLANs and their descriptions on devices from various vendors.

* The script should prompt the user to input the VLAN number and its description.

* Upon receiving the input, it should establish SSH connections to the respective devices and apply the configurations accordingly.

* The goal is to automate the VLAN configuration process across heterogeneous network infrastructure.


### Lab guide:
Follow these steps to set up the lab environment:

1. Create a new file named devices.py and add the following code:

```inventory
# Define Arista device details
arista_device = {
    'device_type': 'arista_eos',
    'ip': '172.16.14.214',
    'username': 'admin',
    'password': 'password',
}

# Define Cisco device details
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.14.210',
    'username': 'admin',
    'password': 'admin',
}
```
2. Create a new file named vlan.py and add the following code:

```python
import os
from netmiko import ConnectHandler
from devices import *

def clear_screen():
    os.system('clear')

def validate_vlan_number(vlan_number):
    while True:
        try:
            vlan_number = int(vlan_number)
            if 1 <= vlan_number <= 3967:  # Updated range to 1-3967
                return vlan_number
            else:
                print("VLAN number must be in the range of 1-3967.")  # Updated error message
        except ValueError:
            print("Invalid VLAN number. Please enter a valid number.")
        vlan_number = input("Please enter VLAN number (1-3967): ")  # Updated prompt

def connection_test(device, device_type):
    try:
        ssh_conn = ConnectHandler(**device)
        print("#"*100)
        print(f"Connected to {device_type} device successfully with IP address: {device['ip']}")
        return ssh_conn
    except Exception as e:
        print(f"Failed to connect to {device_type} device: {e}")
        return None

def configure_device(ssh_conn, config_commands, device_type, vlan_number, vlan_description):
    if ssh_conn:
        print(f'Configuring VLAN "{vlan_number}" with description "{vlan_description}" on {device_type} device...')
        try:
            ssh_conn.enable()
            output = ssh_conn.send_config_set(config_commands)
            print(output)
            # Validate configuration
            validation_command = f'show vlan id {vlan_number}'
            validation_output = ssh_conn.send_command(validation_command)
            print("Validation Output:", validation_output)
            if vlan_description in validation_output:
                print(f"\nVLAN configured successfully on {device_type} device.")
            else:
                print(f"\nFailed to configure VLAN on {device_type} device.")
            ssh_conn.disconnect()
        except Exception as e:
            print(f"Failed to configure VLAN on {device_type} device: {e}")

if __name__ == "__main__":
    clear_screen()
    # Take input for VLAN configuration
    vlan_number = input("Please enter VLAN number: ")
    vlan_number = validate_vlan_number(vlan_number)

    vlan_description = input("Please enter VLAN description: ")

    # Define VLAN configuration commands for Arista device
    arista_config = [
        f'vlan {vlan_number}',
        f'name {vlan_description}',
    ]

    # Test connection to Arista device
    arista_ssh = connection_test(arista_device, "arista_eos")
    if arista_ssh:
        configure_device(arista_ssh, arista_config, "Arista", vlan_number, vlan_description)
    
    # Define VLAN configuration commands for Cisco device
    cisco_config = [
        f'vlan {vlan_number}',
        f'name {vlan_description}',
    ]

    # Test connection to Cisco device
    cisco_ssh = connection_test(cisco_device, "cisco_ios")
    if cisco_ssh:
        configure_device(cisco_ssh, cisco_config, "Cisco", vlan_number, vlan_description)
```
3. Verify the current VLAN status in Cisco NX-OS by running the following command:

```code
show vlan
```

![alt text](image-27.png)

4. To verify the current VLAN status in Arista EOS, execute the following command:
```code
show vlan
```

![alt text](image-28.png)

5. Execute the Python script by running the following command:
```code
python3 vlan.py
```

![alt text](image-29.png)

6. Please enter a VLAN number between 1 and 3096. This restriction is because Cisco NX-OS reserves VLANs above 3096.

    After that, input the description you wish to configure on the interface, and hit Enter again.





![alt text](image-30.png)

Output Explanation:

The provided output displays the configuration commands for the Arista EOS device. These commands represent the VLAN configuration applied to the device.
    
![alt text](image-31.png)

Below are the Cisco IOS device configuration commands displayed in the output. These commands represent the VLAN configuration applied to the device.

![alt text](image-32.png)

7. After executing, you can verify the current VLAN status in Cisco NX-OS by running the following command:
```code
show vlan
```

![alt text](image-33.png)

8. To verify the current VLAN status in Arista EOS, execute the following command:

```code
show vlan
```
![alt text](image-34.png)
