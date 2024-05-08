import os
from netmiko import ConnectHandler
from devices import *

def clear_screen():
    os.system('clear')

def connection_test(device, device_type):
    try:
        ssh_conn = ConnectHandler(**device)
        print("#"*100)
        print(f"Connected to {device_type} device successfully with IP address: {device['ip']}")
        return ssh_conn
    except Exception as e:
        print(f"Failed to connect to {device_type} device: {e}")
        return None

def configure_device(ssh_conn, config_commands, device_type, vlan_number, vlan_description):
    if ssh_conn:
        print(f'Configuring VLAN "{vlan_number}" with description "{vlan_description}" on {device_type} device...')
        try:
            ssh_conn.enable()
            output = ssh_conn.send_config_set(config_commands)
            print(output)
            # Validate configuration
            validation_command = f'show vlan id {vlan_number}'
            validation_output = ssh_conn.send_command(validation_command)
            print("Validation Output:", validation_output)
            if vlan_description in validation_output:
                print(f"\nVLAN configured successfully on {device_type} device.")
            else:
                print(f"\nFailed to configure VLAN on {device_type} device.")
            ssh_conn.disconnect()
        except Exception as e:
            print(f"Failed to configure VLAN on {device_type} device: {e}")

if __name__ == "__main__":
    clear_screen()
    # Take input for VLAN configuration
    vlan_number = input("Please enter VLAN number: ")
    vlan_description = input("Please enter VLAN description: ")

    # Define VLAN configuration commands for Arista device
    arista_config = [
        f'vlan {vlan_number}',
        f'name {vlan_description}',
    ]

    # Test connection to Arista device
    arista_ssh = connection_test(arista_device, "arista_eos")
    if arista_ssh:
        configure_device(arista_ssh, arista_config, "Arista", vlan_number, vlan_description)
    
    # Define VLAN configuration commands for Cisco device
    cisco_config = [
        f'vlan {vlan_number}',
        f'name {vlan_description}',
    ]

    # Test connection to Cisco device
    cisco_ssh = connection_test(cisco_device, "cisco_ios")
    if cisco_ssh:
        configure_device(cisco_ssh, cisco_config, "Cisco", vlan_number, vlan_description)
