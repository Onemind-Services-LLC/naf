# configurations.py

cisco_config = {
    'loopback_ip': '11.11.11.1',
    'point_to_point_interface': 'GigabitEthernet1',
    'point_to_point_ip': '10.0.0.1',
    'ospf_process_id': 1,
    'ospf_networks': ['10.0.0.0 0.0.0.255','11.11.11.0 0.0.0.255']
}

arista_config = {
    'loopback_ip': '22.22.22.22',
    'point_to_point_interface': 'Ethernet3',
    'point_to_point_ip': '10.0.0.2',
    'ospf_process_id': 1,
    'ospf_networks': ['10.0.0.0 0.0.0.255','22.22.22.0 0.0.0.255']
}
