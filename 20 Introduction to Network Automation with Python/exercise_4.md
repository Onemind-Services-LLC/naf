## Exercise:
### Problem Statement:
Create a Python program that does the following:
- Executes show version on cisco nexus switch
- Parses the output into a structured format
- Use textfsm for this exercise

### Solution
- create a pyton program with name `parse_command.py`

```py
import json
from device_vars import *
from netmiko import ConnectHandler
from rich import print

if __name__ == "__main__":
    device_details = [nexus_site1]
    for device in device_details:
        print(device)
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command('show version', use_textfsm=True)
        print(output)

```

![alt text](image-15.png)

#### Try parsing another command like "show ip interface brief"

```py
import json
from device_vars import *
from netmiko import ConnectHandler
from rich import print

if __name__ == "__main__":
    device_details = [nexus_site1]
    for device in device_details:
        print(device)
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command('show ip interface brief', use_textfsm=True)
        print(output)
```

Expected output

```yaml
[
    {'vrf': 'default', 'interface': 'Vlan10', 'ip_address': '192.168.1.1', 'status': 'admin-up', 'link': 'link-up', 'proto': 'protocol-up'},
    {'vrf': 'default', 'interface': 'Eth1/1', 'ip_address': '10.10.10.2', 'status': 'admin-up', 'link': 'link-up', 'proto': 'protocol-up'},
    {'vrf': 'default', 'interface': 'Eth1/3', 'ip_address': '10.10.10.6', 'status': 'admin-up', 'link': 'link-up', 'proto': 'protocol-up'}
]
```