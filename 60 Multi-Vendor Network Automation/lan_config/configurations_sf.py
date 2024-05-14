# configurations_sf.py

vyos1_config = {
    'device_ip': '172.16.14.216',
    'ospf_network': ['10.10.10.32/30','2.2.2.2/32'],
}

vyos2_config = {
    'device_ip': '172.16.14.215',
    'ospf_network': ['10.10.10.36/30'],
}

arista_config ={
    'ospf_network': ['10.10.10.16/30','10.10.10.32/30','10.10.10.36/30','3.3.3.3/32']
}

palo_alto_config= {
    'device_ip': '172.16.14.213',
    'router_id' : "10.10.10.21",
    'interfaces' :['ethernet1/1']
}