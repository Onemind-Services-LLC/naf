### Write a custom Python module for Ansible that interacts with network devices to retrieve interface information. This module will use the Netmiko library, which provides a simple framework for executing commands on network devices via SSH

```py
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

```yaml
---
- hosts: network_devices
  tasks:
    - name: Retrieve Interface Information
      network_interface_info:
        host: "172.16.14.110"
        username: "admin"
        password: "admin"
      register: interface_info

    - debug:
        var: interface_info
```
