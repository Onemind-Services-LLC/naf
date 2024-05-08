# Multi-Vendor Network Automation: VLAN Configuration

**This repository contains a Python script (`vlan.py`) that automates VLAN configuration on Arista EOS and Cisco IOS devices using the Netmiko library.**


### Features

* Supports Arista EOS and Cisco IOS devices.
* Automates VLAN configuration with user-specified number and description.
* Validates VLAN configurations on each device.
* Provides clear output of configuration steps and validation results.

### Prerequisites

* Python 3 installed.
* Netmiko library installed (`pip install netmiko`).

### File Structure

* `devices.py`: Stores device details (IP addresses, usernames, passwords).
* `vlan.py`: Python script for VLAN configuration automation.

### Device Definitions (devices.py)

The `devices.py` file defines dictionaries containing details for the Arista EOS and Cisco IOS devices:

```python
arista_device = {
    'device_type': 'arista_eos',
    'ip': '172.16.14.111',
    'username': 'admin',
    'password': 'admin',
}

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.14.119',
    'username': 'admin',
    'password': 'admin',
}
```
**Device Definition Keys:**

* `device_type`: Specifies the type of network device (arista_eos or cisco_ios).
* `ip`: The device's IP address.
* `username`: Username for SSH authentication.
* `password`: Password for SSH authentication.

## Script Functionality (vlan.py)

The `vlan.py` script performs the following tasks:

### Imports

- **os:** Provides functionality for interacting with the operating system.
- **netmiko:** Facilitates SSH connections and command execution on network devices.
- **devices.py:** Contains device details such as IP addresses, usernames, and passwords.

### Functions

- **clear_screen():** Clears the terminal screen.
- **connection_test(device, device_type):** Establishes an SSH connection to the device and returns the connection object.
- **configure_device(ssh_conn, config_commands, device_type, vlan_number, vlan_description):** Configures VLANs on the device, validates the configuration, and displays the results.

### Execution Logic

1. **Clears the Screen:** The script clears the terminal screen using the `clear_screen()` function.
2. **Prompts for VLAN Details:** The user is prompted to enter the VLAN number and description.
3. **Arista EOS Configuration:**
   - Establishes an SSH connection to the Arista EOS device.
   - Configures and validates the VLAN.
   - Displays configuration steps and validation results.

4. **Cisco IOS Configuration:** (Similar steps as Arista EOS)

### Running the Script

To run the script:

1. Open `vlan.py` in your Integrated Development Environment (IDE) such as Visual Studio Code.
2. Execute the script by running `python vlan.py` in the terminal.
3. Enter the VLAN details as prompted.
4. View the configuration and validation output.

