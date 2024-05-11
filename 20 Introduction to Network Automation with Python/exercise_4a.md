## Exercise:
### Problem Statement:
Write the parsed output in the previous exercise to an excel sheet.

### Solution
- Create a python file with name 'parse_save.py'

```py
from device_vars import *
from netmiko import ConnectHandler
from rich import print

if __name__ == "__main__":
    device_details = [nexus_site1, vmx1_site1]
    for device in device_details:
        print(device)
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command('show interfaces', use_textfsm=True)
        print(output)

```
![alt text](image-17.png)

### Let's write the parsed output to an excel sheet

```py
from device_vars import *
from netmiko import ConnectHandler
from rich import print
import pandas as pd

if __name__ == "__main__":
    device_details = [vmx1_site1]
    for device in device_details:
        print(device)
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command('show interfaces', use_textfsm=True)
        print(output)
        df = pd.DataFrame(output)
        print(df)
        df.to_excel('junos.xlsx', index=False)
```

![alt text](image-18.png)

![alt text](image-19.png)

