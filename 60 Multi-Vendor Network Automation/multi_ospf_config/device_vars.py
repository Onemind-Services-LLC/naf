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
    # "pa_site2": {
    #     "device_type": "paloalto_panos",
    #     "host": "172.16.14.213",
    #     "username": "admin",
    #     "password": "Test12345",
    #     "port": 22,
    #     "secret": "Test12345"
    # },
    # "arista1_site2": {
    #     "device_type": "arista_eos",
    #     "host": "172.16.14.214",
    #     "username": "admin",
    #     "password": "password",
    #     "port": 22,
    #     "secret": "admin",
    #     "timeout": 60
    # }
    # "vyos1_site2": {
    #     "device_type": "vyos",
    #     "host": "172.16.14.215",
    #     "username": "vyos",
    #     "password": "vyos",
    #     "port": 22,
    #     "secret": "admin"
    # },
    # "vyos2_site2": {
    #     "device_type": "vyos",
    #     "host": "172.16.14.216",
    #     "username": "vyos",
    #     "password": "vyos",
    #     "port": 22,
    #     "secret": "admin"
    # },
    # "nxosv9000": {
    #     'device_type': 'cisco_nxos',
    #     'host':   'sandbox-nxos-1.cisco.com',
    #     'username': 'admin',
    #     'password': 'Admin_1234!',
    #     'port' : 22,
    #     'secret': 'Admin_1234!',
}
