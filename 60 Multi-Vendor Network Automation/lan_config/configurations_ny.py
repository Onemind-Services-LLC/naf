# configurations.py

cisco_config = {
    'ospf_interfaces': ['Ethernet1/1','loopback0'],
    'ospf_process_id': 1
}

juniper_config = {
    'ospf_interfaces': ['ge-0/0/0.0','ge-0/0/2.0'],
    'ospf_process_id': 1,
}

palo_alto_config= {
    'device_ip': '172.16.14.212',
    'router_id' : "10.10.10.13",
    'interfaces' :['ethernet1/1']
}