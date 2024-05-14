# device_vars.py

devices_vars = {
    "nexus_site1": {
        "device_type": "cisco_nxos",
        "host": "172.16.14.210",
        "username": "admin",
        "password": "admin",
        "port": 22,
        "secret": "admin",
        "timeout": 240
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
}
