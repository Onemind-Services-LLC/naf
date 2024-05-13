# Multi-Vendor Network Automation: OSPF Configuration

*This repository contains a Python script (`ospf_config.py`) that automates OSPF configuration on Juniper EOS and Cisco IOS devices using the Netmiko library. Palo alto device with REST API.*

### Problem Statement:
* Need to create reachability from loopback interface at New York site and San Francisco palo alto device loopback.

### Solution
* We will create ospf between Cisco NXOS and Juniper OS device at newyork site.
* We will create ospf between Juniper OS and Palo alto device at newyork site.
* We will create OSPF between Polo alto at newyork site and Palo alto San Francisco site.
* We will be able to recieve San Francisco loopback at newyork nxos.

### Lab guide:
Steps:

```python
# device_vars.py

devices_vars = {
    "nexus_site1": {
        "device_type": "cisco_nxos",
        "host": "172.16.14.210",
        "username": "admin",
        "password": "admin",
        "port": 22,
        "secret": "admin",
        "timeout": 60
    },
    "vmx1_site1": {
        "device_type": "juniper_junos",
        "host": "172.16.14.211",
        "username": "root",
        "password": "Juniper",
        "port": 22,
        "secret": "admin"
    },
    "pa_site1": {
        "device_type": "paloalto_panos",
        "host": "172.16.14.212",
        "username": "admin",
        "password": "Test12345",
        "port": 22,
        "secret": "Test12345"
    },
    "pa_site2": {
        "device_type": "paloalto_panos",
        "host": "172.16.14.213",
        "username": "admin",
        "password": "Test12345",
        "port": 22,
        "secret": "Test12345"
    }
}
```

