# device_vars_sf.py

devices_vars = {
    "pa_site2": {
        "device_type": "paloalto_panos",
        "host": "172.16.14.213",
        "username": "admin",
        "password": "Test12345",
        "port": 22,
        "secret": "Test12345"
    },
    "arista1_site2": {
        "device_type": "arista_eos",
        "host": "172.16.14.214",
        "username": "admin",
        "password": "password",
        "port": 22,
        "secret": "admin",
        "timeout": 60
    },
    "vyos1_site2": {
        "device_type": "vyos",
        "host": "172.16.14.215",
        "username": "vyos",
        "password": "vyos",
        "port": 22,
        "secret": "admin"
    },
    "vyos2_site2": {
        "device_type": "vyos",
        "host": "172.16.14.216",
        "username": "vyos",
        "password": "vyos",
        "port": 22,
        "secret": "admin"
    }
}
