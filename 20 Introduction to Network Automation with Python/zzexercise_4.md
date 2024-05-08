# Connect to devices using NETMIKO

pip install netmiko

## Define lab inventory
```py
csr1000v = {
    'device_type': 'cisco_xe',
    'host':   '172.16.14.110',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,                # optional, defaults to 22
    'secret': 'admin',          # optional, defaults to ''
}
```

## Connect to 1 device
```py
from netmiko import ConnectHandler
net_connect = ConnectHandler(**csr1000v)
output = net_connect.send_command('show ip int brief')
print(output)
```

### Explanation:-
- Import ConnectHandler from netmiko module. ConnectHandler is responsible for establishing the SSH read write connection with the device in the background.

- net_connect = ConnectHandler(**csr1000v1)

- - Pass the dictionary of device details that we want to connect to and assign that connection to a variable called net_connect. You could call it anything you want to.

- - To see available methods for net_connect, type print(dir(net_connect)) and this will show you all the methods that you can call against that connection. You can read more about all these methods in the github API documentation of Netmiko. The intention here is to cover the absolute basics to get the ball rolling.

- output = net_connect.send_command(‘show ip int brief’)

- - Call send_command method on net_connect connection handler and pass in the command you want to execute on the device. The result of the command execution will be saved to a variable called output.


## Connect to multiple devices
```py
csr1000v = {
    'device_type': 'cisco_xe',
    'host':   '172.16.14.110',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,                # optional, defaults to 22
    'secret': 'admin',          # optional, defaults to ''
}
arista_veos = {
    'device_type': 'arista_eos',
    'host':   '172.16.14.111',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,
    'secret': 'admin',
}
nxosv9000_1 = {
    'device_type': 'cisco_nxos',
    'host':   '172.16.14.112',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,
    'secret': 'admin',
}
nxosv9000_2 = {
    'device_type': 'cisco_nxos',
    'host':   '172.16.14.113',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,
    'secret': 'admin',
}
```

## Connect to all devices

```py
all_devices = [csr1000v, arista_veos, nxosv9000_1, nxosv9000_2]
for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip int brief | ex unass')
    print(device['host'])
    print("=" * len(device['host']))
    print(output)
```

## Connect and execute multiple commands

If we want to extract multiple commands and multiple devices, we can modify the script a little bit to do so.

For each device in the all_devices list, we will execute each command in the commands list. We are using nested for loops here to achieve the task.

```py
all_devices = [csr1000v1, csr1000v2, iosxrv9000, nxosv9000]
commands = ['show version', 'show ip int br | ex unass', 'show cdp nei']
for device in all_devices:
    net_connect = ConnectHandler(**device)
    print(device['host'])
    print("=" * len(device['host']))
    for command in commands:
        output = net_connect.send_command(command)
        print(output)
```

### Explanation:-
- send_command as the name suggests sends the command to the device and outputs the response to a variable
- send_command method is looking for the device prompt, it keeps on reading the output until the device prompt is found again which is usually when the command execution is completed.
 - Instead of using send_command, there may be scenarios where you need to execute

- send_command_timing
- - You can control the delay in this command in scenarios where you want to copy paste files to and from bootflash and the default wait interval of netmiko is too less specially when you want to work over WAN.
- - Instead of stopping the execution after finding the device prompt, the script works on predefined delay intervals. 

- send_command_expect
- - Interactive CLI commands where you need to hit return / enter. So instead of stopping the command execution after default device prompt is seen or a specific time. The command execution is controlled by the pattern you specify and expect to see the entire order of operations.

```
# cisco1#delete flash:/testb.txt
# Delete filename [testb.txt]? 
# Delete flash:/testb.txt? [confirm]y

# Use 'send_command' and the 'expect_string' argument (note, expect_string uses RegEx patterns).
# Netmiko will move-on to the next command when the 'expect_string' is detected.
```

### Here is a showcase of all arguments that you can pass to the netmiko send_command( ) method

```py
def send_command(
    self,
    command_string: str,
    expect_string: Optional[str] = None,
    delay_factor: float = 1.0,
    max_loops: int = 500,
    auto_find_prompt: bool = True,
    strip_prompt: bool = True,
    strip_command: bool = True,
    normalize: bool = True,
    use_textfsm: bool = False,
    textfsm_template: Optional[str] = None,
    use_ttp: bool = False,
    ttp_template: Optional[str] = None,
    use_genie: bool = False,
    cmd_verify: bool = True,
) -> str:
    """Execute command_string on the SSH channel using a pattern-based mechanism. Generally
    used for show commands. By default this method will keep waiting to receive data until the
    network device prompt is detected. The current network device prompt will be determined
    automatically.

    :param command_string: The command to be executed on the remote device.
    :type command_string: str

    :param expect_string: Regular expression pattern to use for determining end of output.
        If left blank will default to being based on router prompt.
    :type expect_string: str

    :param delay_factor: Multiplying factor used to adjust delays (default: 1).
    :type delay_factor: int

    :param max_loops: Controls wait time in conjunction with delay_factor. Will default to be
        based upon self.timeout.
    :type max_loops: int

    :param strip_prompt: Remove the trailing router prompt from the output (default: True).
    :type strip_prompt: bool

    :param strip_command: Remove the echo of the command from the output (default: True).
    :type strip_command: bool

    :param normalize: Ensure the proper enter is sent at end of command (default: True).
    :type normalize: bool

    :param use_textfsm: Process command output through TextFSM template (default: False).
    :type normalize: bool

    :param textfsm_template: Name of template to parse output with; can be fully qualified
        path, relative path, or name of file in current directory. (default: None).

    :param use_ttp: Process command output through TTP template (default: False).
    :type use_ttp: bool

    :param ttp_template: Name of template to parse output with; can be fully qualified
        path, relative path, or name of file in current directory. (default: None).
    :type ttp_template: str

    :param use_genie: Process command output through PyATS/Genie parser (default: False).
    :type normalize: bool

    :param cmd_verify: Verify command echo before proceeding (default: True).
    :type cmd_verify: bool
    """
```

## Enter into enable mode and configure devices

```py
all_devices = [csr1000v1]
for device in all_devices:
    net_connect = ConnectHandler(**device)
    print(dir(net_connect))

## There are tons of methods that you can call on net_connect connection object that we just created.

['RESPONSE_RETURN',
 'RETURN',
 'TELNET_RETURN',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__enter__',
 '__eq__',
 '__exit__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_autodetect_fs',
 '_build_ssh_client',
 '_config_mode',
 '_connect_params_dict',
 '_first_line_handler',
 '_legacy_mode',
 '_lock_netmiko_session',
 '_modify_connection_params',
 '_open',
 '_read_channel',
 '_read_channel_expect',
 '_read_channel_timing',
 '_sanitize_output',
 '_session_locker',
 '_session_log_close',
 '_session_log_fin',
 '_test_channel_read',
 '_timeout_exceeded',
 '_try_session_preparation',
 '_unlock_netmiko_session',
 '_use_ssh_config',
 '_write_channel',
 '_write_session_log',
 'allow_agent',
 'allow_auto_change',
 'alt_host_keys',
 'alt_key_file',
 'ansi_escape_codes',
 'auth_timeout',
 'banner_timeout',
 'base_prompt',
 'blocking_timeout',
 'check_config_mode',
 'check_enable_mode',
 'cleanup',
 'clear_buffer',
 'close_session_log',
 'commit',
 'config_mode',
 'conn_timeout',
 'device_type',
 'disable_paging',
 'disconnect',
 'enable',
 'encoding',
 'establish_connection',
 'exit_config_mode',
 'exit_enable_mode',
 'fast_cli',
 'find_prompt',
 'global_cmd_verify',
 'global_delay_factor',
 'host',
 'is_alive',
 'keepalive',
 'key_file',
 'key_policy',
 'normalize_cmd',
 'normalize_linefeeds',
 'open_session_log',
 'paramiko_cleanup',
 'passphrase',
 'password',
 'pkey',
 'port',
 'protocol',
 'read_channel',
 'read_until_pattern',
 'read_until_prompt',
 'read_until_prompt_or_pattern',
 'remote_conn',
 'remote_conn_pre',
 'run_ttp',
 'save_config',
 'secret',
 'select_delay_factor',
 'send_command',
 'send_command_expect',
 'send_command_timing',
 'send_config_from_file',
 'send_config_set',
 'serial_login',
 'serial_settings',
 'session_log',
 'session_log_record_writes',
 'session_preparation',
 'session_timeout',
 'set_base_prompt',
 'set_terminal_width',
 'sock',
 'special_login_handler',
 'ssh_config_file',
 'strip_ansi_escape_codes',
 'strip_backspaces',
 'strip_command',
 'strip_prompt',
 'system_host_keys',
 'telnet_login',
 'timeout',
 'use_keys',
 'username',
 'verbose',
 'write_channel']
 ```

For this example, we need to focus on find_prompt() and enable()

1. find_prompt( ) will allow you to print the current prompt.
2. enable( ) will allow you to enter the enable prompt.
3. config( ) will allow you to enter the config prompt and execute config commands.

```py
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.enable()
print(net_connect.find_prompt())
net_connect.config_mode()
print(net_connect.find_prompt())


╰─ python3 script4.py

csr1000v#
csr1000v#
csr1000v(config)#

```
Once you are inside the config mode( ), we can push the configuration changes to command to devices.

```py
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.enable()
    print(net_connect.find_prompt())
    net_connect.config_mode()
    print(net_connect.find_prompt())
    print(net_connect.send_command('do show int description'))
    print("======================================")
    print(net_connect.send_config_set(['interface Gi2', 'description cloudmylab.com']))
    print("======================================")
    print(net_connect.send_command('show int description'))
    print("======================================")

```
```
╰─ python3 script4.py

csr1000v-1#
csr1000v-1#
csr1000v-1(config)#
Interface                      Status         Protocol Description
Gi1                            up             up       MANAGEMENT INTERFACE - DON'T TOUCH ME
Gi2                            admin down     down     Network Interface
Gi3                            admin down     down     Network Interface
======================================
interface Gi2
csr1000v-1(config-if)#description cloudmylab.com
csr1000v-1(config-if)#end
csr1000v-1#
======================================
Interface                      Status         Protocol Description
Gi1                            up             up       MANAGEMENT INTERFACE - DON'T TOUCH ME
Gi2                            admin down     down     cloudmylab.com
Gi3                            admin down     down     Network Interface
======================================

```

### Explanation:-

Enter enable mode  
Enter config mode  
execute “do show int description” because we are inside config mode.  
Push config commands to change the description of Gi2 to cloudmylab.com  
Once the push of config commands is complete, netmiko will automatically exit the config mode.  
Execute ‘show int description’ because we are in enable mode to see the configuration change being applied.  

## How to parse data with netmiko

### TEXTFSM

### GENIE

```
pip install genie
#but genie is also available as a part of pyats framework.
#you could also execute
pip install pyats[full]
```

```py
all_devices = [csr1000v, arista_veos, nxosv9000_1, nxosv9000_2]
for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show version', use_genie=True)
    print(net_connect.host)
    print("*" * len(net_connect.host))
    print(output)
```
```json
sample output here

sandbox-iosxe-latest-1.cisco.com
********************************
{'version': {'xe_version': '17.03.01a', 'version_short': '17.3', 'platform': 'Virtual XE', 'version': '17.3.1a', 'image_id': 'X86_64_LINUX_IOSD-UNIVERSALK9-M', 'label': 'RELEASE SOFTWARE (fc3)', 'os': 'IOS-XE', 'image_type': 'production image', 'compiled_date': 'Wed 12-Aug-20 00:16', 'compiled_by': 'mcpre', 'rom': 'IOS-XE ROMMON', 'hostname': 'csr1000v-1', 'uptime': '1 day, 8 hours, 11 minutes', 'uptime_this_cp': '1 day, 8 hours, 13 minutes', 'returned_to_rom_by': 'reload', 'system_image': 'bootflash:packages.conf', 'last_reload_reason': 'reload', 'license_level': 'ax', 'license_type': 'N/A(Smart License Enabled)', 'next_reload_license_level': 'ax', 'chassis': 'CSR1000V', 'main_mem': '715705', 'processor_type': 'VXE', 'rtr_type': 'CSR1000V', 'chassis_sn': '9ESGOBARV9D', 'number_of_intfs': {'Gigabit Ethernet': '3'}, 'mem_size': {'non-volatile configuration': '32768', 'physical': '3978420'}, 'disks': {'bootflash:.': {'disk_size': '6188032', 'type_of_disk': 'virtual hard disk'}}, 'curr_config_register': '0x2102'}}
sandbox-iosxe-recomm-1.cisco.com
********************************
{'version': {'xe_version': '16.09.03', 'version_short': '16.9', 'platform': 'Virtual XE', 'version': '16.9.3', 'image_id': 'X86_64_LINUX_IOSD-UNIVERSALK9-M', 'label': 'RELEASE SOFTWARE (fc2)', 'os': 'IOS-XE', 'image_type': 'production image', 'compiled_date': 'Wed 20-Mar-19 07:56', 'compiled_by': 'mcpre', 'rom': 'IOS-XE ROMMON', 'hostname': 'csr1000v-1', 'uptime': '2 days, 22 hours, 57 minutes', 'uptime_this_cp': '2 days, 22 hours, 59 minutes', 'returned_to_rom_by': 'reload', 'system_image': 'bootflash:packages.conf', 'last_reload_reason': 'reload', 'license_level': 'ax', 'license_type': 'Default. No valid license found.', 'next_reload_license_level': 'ax', 'chassis': 'CSR1000V', 'main_mem': '2392579', 'processor_type': 'VXE', 'rtr_type': 'CSR1000V', 'chassis_sn': '926V75BDNRJ', 'number_of_intfs': {'Gigabit Ethernet': '3'}, 'mem_size': {'non-volatile configuration': '32768', 'physical': '8113280'}, 'disks': {'bootflash:.': {'disk_size': '7774207', 'type_of_disk': 'virtual hard disk'}, 'webui:.': {'disk_size': '0', 'type_of_disk': 'WebUI ODM Files'}}, 'curr_config_register': '0x2102'}}
sandbox-iosxr-1.cisco.com
*************************
{'operating_system': 'IOSXR', 'software_version': '6.5.3', 'device_family': 'IOS-XRv 9000', 'uptime': '2 weeks 2 days 2 hours 17 minutes'}
sandbox-nxos-1.cisco.com
************************
{'platform': {'name': 'Nexus', 'os': 'NX-OS', 'software': {'system_version': '9.3(3)', 'system_image_file': 'bootflash:///nxos.9.3.3.bin', 'system_compile_time': '12/22/2019 2:00:00 [12/22/2019 14:00:37]'}, 'hardware': {'model': 'Nexus9000 C9300v', 'chassis': 'Nexus9000 C9300v', 'slots': 'None', 'rp': 'None', 'cpu': 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz', 'memory': '16408984 kB', 'processor_board_id': '9N3KD63KWT0', 'device_name': 'sbx_nxosv1', 'bootflash': '4287040 kB'}, 'kernel_uptime': {'days': 11, 'hours': 2, 'minutes': 25, 'seconds': 9}, 'reason': 'Unknown'}}
```

### Format the data into json format

```py
import json
all_devices = [csr1000v, arista_veos, nxosv9000_1, nxosv9000_2]
for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show version', use_genie=True)
    print(net_connect.host)
    print("*" * len(net_connect.host))
    print(json.dumps(output, indent=4, sort_keys=True))
```
```json
sandbox-iosxe-latest-1.cisco.com
********************************
{
    "version": {
        "chassis": "CSR1000V",
        "chassis_sn": "9ESGOBARV9D",
        "compiled_by": "mcpre",
        "compiled_date": "Wed 12-Aug-20 00:16",
        "curr_config_register": "0x2102",
        "disks": {
            "bootflash:.": {
                "disk_size": "6188032",
                "type_of_disk": "virtual hard disk"
            }
        },
        "hostname": "csr1000v-1",
        "image_id": "X86_64_LINUX_IOSD-UNIVERSALK9-M",
        "image_type": "production image",
        "label": "RELEASE SOFTWARE (fc3)",
        "last_reload_reason": "reload",
        "license_level": "ax",
        "license_type": "N/A(Smart License Enabled)",
        "main_mem": "715705",
        "mem_size": {
            "non-volatile configuration": "32768",
            "physical": "3978420"
        },
        "next_reload_license_level": "ax",
        "number_of_intfs": {
            "Gigabit Ethernet": "3"
        },
        "os": "IOS-XE",
        "platform": "Virtual XE",
        "processor_type": "VXE",
        "returned_to_rom_by": "reload",
        "rom": "IOS-XE ROMMON",
        "rtr_type": "CSR1000V",
        "system_image": "bootflash:packages.conf",
        "uptime": "1 day, 8 hours, 13 minutes",
        "uptime_this_cp": "1 day, 8 hours, 14 minutes",
        "version": "17.3.1a",
        "version_short": "17.3",
        "xe_version": "17.03.01a"
    }
}
sandbox-iosxe-recomm-1.cisco.com
********************************
{
    "version": {
        "chassis": "CSR1000V",
        "chassis_sn": "926V75BDNRJ",
        "compiled_by": "mcpre",
        "compiled_date": "Wed 20-Mar-19 07:56",
        "curr_config_register": "0x2102",
        "disks": {
            "bootflash:.": {
                "disk_size": "7774207",
                "type_of_disk": "virtual hard disk"
            },
            "webui:.": {
                "disk_size": "0",
                "type_of_disk": "WebUI ODM Files"
            }
        },
        "hostname": "csr1000v-1",
        "image_id": "X86_64_LINUX_IOSD-UNIVERSALK9-M",
        "image_type": "production image",
        "label": "RELEASE SOFTWARE (fc2)",
        "last_reload_reason": "reload",
        "license_level": "ax",
        "license_type": "Default. No valid license found.",
        "main_mem": "2392579",
        "mem_size": {
            "non-volatile configuration": "32768",
            "physical": "8113280"
        },
        "next_reload_license_level": "ax",
        "number_of_intfs": {
            "Gigabit Ethernet": "3"
        },
        "os": "IOS-XE",
        "platform": "Virtual XE",
        "processor_type": "VXE",
        "returned_to_rom_by": "reload",
        "rom": "IOS-XE ROMMON",
        "rtr_type": "CSR1000V",
        "system_image": "bootflash:packages.conf",
        "uptime": "2 days, 22 hours, 59 minutes",
        "uptime_this_cp": "2 days, 23 hours, 0 minutes",
        "version": "16.9.3",
        "version_short": "16.9",
        "xe_version": "16.09.03"
    }
}
sandbox-iosxr-1.cisco.com
*************************
{
    "device_family": "IOS-XRv 9000",
    "operating_system": "IOSXR",
    "software_version": "6.5.3",
    "uptime": "2 weeks 2 days 2 hours 19 minutes"
}
sandbox-nxos-1.cisco.com
************************
{
    "platform": {
        "hardware": {
            "bootflash": "4287040 kB",
            "chassis": "Nexus9000 C9300v",
            "cpu": "Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz",
            "device_name": "sbx_nxosv1",
            "memory": "16408984 kB",
            "model": "Nexus9000 C9300v",
            "processor_board_id": "9N3KD63KWT0",
            "rp": "None",
            "slots": "None"
        },
        "kernel_uptime": {
            "days": 11,
            "hours": 2,
            "minutes": 26,
            "seconds": 46
        },
        "name": "Nexus",
        "os": "NX-OS",
        "reason": "Unknown",
        "software": {
            "system_compile_time": "12/22/2019 2:00:00 [12/22/2019 14:00:37]",
            "system_image_file": "bootflash:///nxos.9.3.3.bin",
            "system_version": "9.3(3)"
        }
    }
}

```

## Multithreading with Netmiko

```py
import threading  # import python's threading module
from netmiko import ConnectHandler
import time
import logging

def connect_and_fetch(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show version', use_genie=True)
    print(net_connect.host)
    print("*" * len(net_connect.host))
    # print(output)


if __name__ == "__main__":
    threads = []
    all_devices = [csr1000v, arista_veos, nxosv9000_1, nxosv9000_2]
    for device in all_devices:
        # Spawn threads and append to threads list
        th = threading.Thread(target=connect_and_fetch, args=(device,))
        threads.append(th)
    
    # iterate through threads list and start each thread to perform its task
    for thread in threads:
        thread.start()

    #Once all threads have done the work, join the output of all threads to return the final output.
    for thread in threads:
        thread.join()
```

### IMPROVEMENTS:-

The code above works fast sure but is it a good code, no, it is not. There are some loopholes here that we can fix and take care of especially when we are spawning multiple threads and can run into issues like

1. We are spawning all threads ahead of time. So if you have hundreds of devices to connect to, you are essentially spawning those many threads before the threads even start to do something.

2. The above doesn’t limit the number of threads you can spawn parallel. If you have a thousand devices, it will try to spawn 1000 threads and your application may crash if it’s unable to handle so many threads without proper error handling.

```py
if __name__ == "__main__":
    max_threads = 2 # Set max threads to 2. You can see what number works best for you.
    threads = []
    all_devices = [csr1000v, arista_veos, nxosv9000_1, nxosv9000_2]
    for device in all_devices:
        # Spawn threads and append to threads list
        th = threading.Thread(target=connect_and_fetch, args=(device,))
        threads.append(th)
        th.start()
        #After each thread is started and added to dictionary, we are checking if the total number
        #of threads is more than what we have configured. If yes, wait or else continue
        while True:
            alive_cnt = 0
            for t in self.threads:
                if t.is_alive():
                    alive_cnt += 1
            if alive_cnt >=max_threads:
                logging.info('Do not spawn new thread, already reached max limit of alive threads [%s]' % alive_cnt)
                time.sleep(2)
                continue
            break

    #Once all threads have done the work, join the output of all threads to return the final output.
    for thread in threads:
        thread.join()

```

3. Now that we have the basics right, there is a way to reduce the number of lines of manual coding that we had to do above and let python handle all this for you.

```py
import concurrent.futures

if __name__ == "__main__":
    all_devices = [csr1000v, arista_veos, nxosv9000_1, nxosv9000_2]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(connect_and_fetch, all_devices)

```
