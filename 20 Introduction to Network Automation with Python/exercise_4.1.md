```py
from netmiko import ConnectHandler

csr1000v = {
    'device_type': 'cisco_xe',
    'host':   '172.16.14.110',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,
    'secret': 'admin'
}

def run_commands_on_router(device_info, commands):
    try:
        with ConnectHandler(**device_info) as ssh:
            ssh.enable()  # Enter privileged mode
            output = ""
            for command in commands:
                output += ssh.send_command(command) + "\n"
            return output
    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == "__main__":
    commands_to_run = [
        "show version",
        "show ip interface brief",
    ]
    
    router_output = run_commands_on_router(csr1000v, commands_to_run)
    if router_output:
        print("Router Output:")
        print(router_output)
    else:
        print("Failed to retrieve router output.")
```

This program connects to a router using the netmiko library and runs specified commands on it. Here's a breakdown:

- It sets up the router's details like IP address, username, and password.
- The run_commands_on_router function connects to the router, enters privileged mode, runs the specified commands, and returns the output.
- In the main part of the program, you list the commands you want to run on the router.
- The program executes the commands on the router and prints the output.
