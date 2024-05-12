import requests
import xml.etree.ElementTree as ET
from netmiko import ConnectHandler
from device_vars import devices_vars
from configurations import cisco_config, juniper_config

def check_ssh_connectivity(device_name, device_info):
    try:
        # Create connection handler
        net_connect = ConnectHandler(**device_info)
        net_connect.disconnect()
        print(f"SSH connection to {device_name} ({device_info['host']}) successful.")
        return True

    except Exception as e:
        print(f"Failed to establish SSH connection to {device_name} ({device_info['host']}): {e}")
        return False

def apply_ospf_config_cisco(device_name, device_info, ospf_config):
    try:
        # Create connection handler
        net_connect = ConnectHandler(**device_info)

        # Prepare OSPF configuration commands for Cisco devices
        ospf_commands = [
            f"router ospf {ospf_config['ospf_process_id']}"
        ]

        # Iterate over OSPF interfaces and add configuration commands
        for interface in ospf_config['ospf_interfaces']:
            ospf_commands.append(f"interface {interface}")
            ospf_commands.append(f"ip router ospf 1 area 0.0.0.0")

        # Send OSPF configuration commands
        output = net_connect.send_config_set(ospf_commands)
        print(f"OSPF configuration applied on {device_name} ({device_info['host']}) successfully:")
        print(output)

        # Disconnect from device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to apply OSPF configuration on {device_name} ({device_info['host']}): {e}")

def apply_ospf_config_juniper(device_name, device_info, ospf_config):
    try:
        # Create connection handler
        net_connect = ConnectHandler(**device_info)

        # Prepare OSPF configuration commands for Juniper devices
        ospf_commands = [
            "configure"
        ]

        # Iterate over OSPF interfaces and add configuration commands
        for interface in ospf_config['ospf_interfaces']:
            ospf_commands.append(f"set protocols ospf area 0.0.0.0 interface {interface}")

        # Add commit command
        ospf_commands.append("commit")

        # Send OSPF configuration commands
        output = net_connect.send_config_set(ospf_commands, read_timeout=30)
        print(f"OSPF configuration applied on {device_name} ({device_info['host']}) successfully:")
        print(output)

        # Disconnect from device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to apply OSPF configuration on {device_name} ({device_info['host']}): {e}")

def generate_palo_alto_api_key(device_name, device_info):
    try:
        # API endpoint for generating API key
        api_endpoint = f"https://{device_info['host']}/api/?type=keygen&user={device_info['username']}&password={device_info['password']}"

        # Send POST request to the API endpoint
        response = requests.post(api_endpoint, verify=False)
        print(response)
        response.raise_for_status()  # Raise an exception for any HTTP error

        # Parse XML response
        root = ET.fromstring(response.text)

        # Find the API key element
        api_key_element = root.find('.//key')
        if api_key_element is not None:
            api_key = api_key_element.text
            print(f"API key generated successfully for {device_name} ({device_info['host']}): {api_key}")
            return api_key
        else:
            print(f"Failed to generate API key for {device_name} ({device_info['host']}): No API key found.")
            return None

    except Exception as e:
        print(f"Failed to generate API key for {device_name} ({device_info['host']}): {e}")
        return None

def get_virtual_routers(api_endpoint, api_key):
    try:
        headers = {
            "X-PAN-KEY": api_key,
            "Accept": "application/json"
        }
        response = requests.get(api_endpoint, headers=headers, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            virtual_routers = data.get('result', {}).get('entry', [])
            return virtual_routers
        else:
            print(f"Failed to retrieve Virtual Routers. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Failed to retrieve Virtual Routers: {e}")
        return None

def modify_virtual_router(api_endpoint, api_key, vr_name):
    try:
        # Prepare the modified virtual router payload
        modified_vr_payload = {
            "entry": {
  "@name": "default",
  "interface": {
    "member": ["ethernet1/1", "ethernet1/2", "ethernet1/3"]
  },
  "protocol": {
    "ospf": {
            "enable": "yes",
    "router-id": "10.10.10.13",
    },
  },
  }
}
        

        # Send PUT request to modify the virtual router
        headers = {
            "X-PAN-KEY": api_key,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        params = {
            "name": vr_name  # Add the virtual router name as a query parameter
        }
        response = requests.put(api_endpoint, json=modified_vr_payload, params=params, headers=headers, verify=False)
        
        if response.status_code == 200:
            print(f"Virtual Router '{vr_name}' modified successfully.")
        else:
            print(f"Failed to modify Virtual Router '{vr_name}'. Status code: {response.json()}")

    except Exception as e:
        print(f"Failed to modify Virtual Router '{vr_name}': {e}")

if __name__ == "__main__":
    # Check SSH connectivity and apply OSPF configuration to each device
    for device_name, device_info in devices_vars.items():
        if check_ssh_connectivity(device_name, device_info):
            if "cisco" in device_info["device_type"]:
                apply_ospf_config_cisco(device_name, device_info, cisco_config)
            elif "juniper" in device_info["device_type"]:
                apply_ospf_config_juniper(device_name, device_info, juniper_config)
            elif "paloalto" in device_info["device_type"]:
                api_key = generate_palo_alto_api_key(device_name, device_info)
                if api_key:
                    api_endpoint = f"https://{device_info['host']}/restapi/v9.1/Network/VirtualRouters"
                    virtual_routers = get_virtual_routers(api_endpoint, api_key)
                    if virtual_routers:
                        print(f"Virtual Routers for {device_name} ({device_info['host']}):")
                        for router in virtual_routers:
                            print(router)
                        # # Modify virtual router to disable OSPF
                        vr_name = 'default'  # Modify accordingly
                        modify_virtual_router(api_endpoint, api_key, vr_name)
