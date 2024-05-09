# vlan.py

from netmiko import ConnectHandler
from devices_details import cisco_device, arista_device
from configurations import cisco_config, arista_config
import time

def test_device_connectivity(device):
    try:
        ssh_conn = ConnectHandler(**device)
        ssh_conn.disconnect()
        print(f"Successfully connected to {device['device_type']} device with IP address: {device['ip']}")
        return True
    except Exception as e:
        print(f"Failed to connect to {device['device_type']} device: {e}")
        return False

def configure_loopback(device, loopback_ip):
    try:
        ssh_conn = ConnectHandler(**device)
        loopback_config = [
            f'interface loopback 1',
            f'ip address {loopback_ip} 255.255.255.255',
            'no shutdown'
        ]
        ssh_conn.enable()
        output = ssh_conn.send_config_set(loopback_config)
        print(output)
        print(f"Loopback interface configured successfully on {device['device_type']} device.")
        ssh_conn.disconnect()
        return True
    except Exception as e:
        print(f"Failed to configure loopback interface on {device['device_type']} device: {e}")
        return False

def configure_point_to_point(device, point_to_point_interface, point_to_point_ip):
    try:
        ssh_conn = ConnectHandler(**device)
        point_to_point_config = [
            f'interface {point_to_point_interface}',
            'no switchport',
            f'ip address {point_to_point_ip} 255.255.255.252',
            'no shutdown'
        ]
        ssh_conn.enable()
        output = ssh_conn.send_config_set(point_to_point_config)
        print(output)
        print(f"Point-to-point interface configured successfully on {device['device_type']} device.")
        ssh_conn.disconnect()
        return True
    except Exception as e:
        print(f"Failed to configure point-to-point interface on {device['device_type']} device: {e}")
        return False

def configure_ospf(device, ospf_process_id, ospf_networks):
    try:
        ssh_conn = ConnectHandler(**device)
        ospf_config = [
            f'router ospf {ospf_process_id}',
            *[f'network {network} area 0' for network in ospf_networks]
        ]
        ssh_conn.enable()
        output = ssh_conn.send_config_set(ospf_config)
        print(output)
        print(f"OSPF configured successfully on {device['device_type']} device.")
        ssh_conn.disconnect()
        return True
    except Exception as e:
        print(f"Failed to configure OSPF on {device['device_type']} device: {e}")
        return False

def verify_loopback(device, loopback_ip):
    try:
        ssh_conn = ConnectHandler(**device)
        output = ssh_conn.send_command("show ip interface brief | include Loopback1")
        print(output)
        if loopback_ip in output:
            print(f"Loopback interface is up and running on {device['device_type']} device.")
            return True
        else:
            print(f"Loopback interface is not configured properly on {device['device_type']} device.")
            return False
    except Exception as e:
        print(f"Failed to verify loopback interface on {device['device_type']} device: {e}")
        return False

def verify_ospf(device, ospf_process_id, ospf_networks):
    try:
        ssh_conn = ConnectHandler(**device)
        output = ssh_conn.send_command("show ip ospf neighbor")
        print(output)
        if "FULL" in output:
            print(f"OSPF neighbors are fully adjacent on {device['device_type']} device.")
            return True
        else:
            print(f"OSPF neighbors are not fully adjacent on {device['device_type']} device.")
            return False
    except Exception as e:
        print(f"Failed to verify OSPF on {device['device_type']} device: {e}")
        return False

if __name__ == "__main__":
    cisco_connectivity = test_device_connectivity(cisco_device)
    arista_connectivity = test_device_connectivity(arista_device)

    if cisco_connectivity and arista_connectivity:
        print("\nDevice connectivity test successful. Proceeding with configuration.")
        print('#'*100)
        print('Configuring cisco device')
        print('#'*100)
        configure_loopback(cisco_device, cisco_config['loopback_ip'])
        configure_point_to_point(cisco_device, cisco_config['point_to_point_interface'], cisco_config['point_to_point_ip'])
        configure_ospf(cisco_device, cisco_config['ospf_process_id'], cisco_config['ospf_networks'])
        print('#'*100)
        print('Configuring aristra device')
        print('#'*100)
        configure_loopback(arista_device, arista_config['loopback_ip'])
        configure_point_to_point(arista_device, arista_config['point_to_point_interface'], arista_config['point_to_point_ip'])
        configure_ospf(arista_device, arista_config['ospf_process_id'],arista_config['ospf_networks'])
        print('#'*100)
        print('Verifing device config')
        print('#'*100)
        # Verification tasks
        verify_loopback(cisco_device, cisco_config['loopback_ip'])
        verify_loopback(arista_device, arista_config['loopback_ip'])

        # Add a delay before verifying OSPF status
        print("\nWaiting for 60 seconds before verifying OSPF status...")
        time.sleep(60)

        verify_ospf(cisco_device, cisco_config['ospf_process_id'], cisco_config['ospf_networks'])
        verify_ospf(arista_device, arista_config['ospf_process_id'],arista_config['ospf_networks'])
    else:
        print("Device connectivity test failed. Check network connectivity and try again.")
