### Write a custom Python module for Ansible that interacts with network devices to retrieve interface information. This module will use the Netmiko library, which provides a simple framework for executing commands on network devices via SSH

- In your ansible working directory, create a folder named "library"
- Inside the library folder, create a python file named "network_interface_info.py"
- Copy paste the below code in that python file

```py
#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from netmiko import ConnectHandler
import re

def get_interface_info(host, username, password):
    """Retrieve information about interfaces on the network device."""
    device = {
        'device_type': 'cisco_nxos',
        'host': host,
        'username': username,
        'password': password
    }

    try:
        # Connect to the network device
        net_connect = ConnectHandler(**device)

        # Send command to retrieve interface information
        output = net_connect.send_command('show ip interface brief')
        output = re.findall('\\n(\S+)\s+(\S+)\s+\S+-(\S+)', output)
        # return output
        # Parse interface information
        interface_info = {}
        for item in output:
            interface_info[item[0]] = {
                'ip_address': item[1],
                'status': item[2]
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

- Create a new playbook called "retreive_interfaces.yaml" in the same level as library folder
- 

```yaml
---

- name: "retreive_interfaces.yaml"
  hosts: nexus-site1
  gather_facts: no
  tasks:
    - name: Retrieve Interface Information
      network_interface_info:
        host: "172.16.14.210"
        username: "admin"
        password: "admin"
        register: interface_info

    - debug:
        var: interface_info
```

```text

root@5e9393be42b8:/python_automation# ansible-playbook -i inventory.ini retreive_interfaces.yaml 

PLAY [retreive_interfaces.yaml] *******************************************************************************************************************************************************************************************************************

TASK [Retrieve Interface Information] *************************************************************************************************************************************************************************************************************
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
<unknown>:21: SyntaxWarning: invalid escape sequence '\S'
ok: [nexus-site1]

TASK [debug] **************************************************************************************************************************************************************************************************************************************
ok: [nexus-site1] => {
    "interface_info": {
        "changed": false,
        "failed": false,
        "interface_info": {
            "Eth1/1": {
                "ip_address": "10.10.10.2",
                "status": "up"
            },
            "Eth1/3": {
                "ip_address": "10.10.10.6",
                "status": "up"
            },
            "Vlan10": {
                "ip_address": "192.168.1.1",
                "status": "up"
            }
        }
    }
}

PLAY RECAP ****************************************************************************************************************************************************************************************************************************************
nexus-site1                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  

```
