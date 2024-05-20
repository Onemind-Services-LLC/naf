## Multithreading with Netmiko
### While using automation can be extremely satisfying and you can see extremely high efficiency while collecting data from multiple devices or pushing configs
However, when the code is scallig to tens of thousands of devices, sequential read and write to a network device which has IO delay can incur significant delays
Hence we are going to explore the usage of executing commands on multiple devices in parallel to speed up the overall process by manyfolds.

Create a file called multithreading_netmiko.py

```py
import threading  # import python's threading module
from netmiko import ConnectHandler
from device_vars import *

def connect_and_fetch(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show version')
    print(net_connect.host)
    print("*" * len(net_connect.host))
    print(output)

if __name__ == "__main__":
    threads = []
    all_devices = [nexus_site1, vyos1_site2, vyos2_site2]
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
import threading  # import python's threading module
from netmiko import ConnectHandler
from device_vars import *
import time


def connect_and_fetch(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show version')
    print(net_connect.host)
    print("*" * len(net_connect.host))

if __name__ == "__main__":
    max_threads = 2 # Set max threads to 2. You can see what number works best for you.
    threads = []
    all_devices = [nexus_site1, vyos1_site2, vyos2_site2]
    for device in all_devices:
        # Spawn threads and append to threads list
        th = threading.Thread(target=connect_and_fetch, args=(device,))
        threads.append(th)
        th.start()
        #After each thread is started and added to dictionary, we are checking if the total number
        #of threads is more than what we have configured. If yes, wait or else continue
        while True:
            alive_cnt = 0
            for t in threads:
                if t.is_alive():
                    alive_cnt += 1
            if alive_cnt >=max_threads:
                print('Do not spawn new thread, already reached max limit of alive threads [%s]' % alive_cnt)
                time.sleep(2)
                continue
            break

    #Once all threads have done the work, join the output of all threads to return the final output.
    for thread in threads:
        thread.join()
```

```text
cml@cml:~/python_automation$ python3 multithreading_netmiko.py 
Do not spawn new thread, already reached max limit of alive threads [2]
Do not spawn new thread, already reached max limit of alive threads [2]
172.16.14.210
*************
Do not spawn new thread, already reached max limit of alive threads [2]
172.16.14.215
*************
172.16.14.216
*************
cml@cml:~/python_automation$ 
```

3. Now that we have the basics right, there is a way to reduce the number of lines of manual coding that we had to do above and let python handle all this for you.

```py
from netmiko import ConnectHandler
from device_vars import *
import time
import concurrent.futures

def connect_and_fetch(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show version')
    print(net_connect.host)
    print("*" * len(net_connect.host))
    print(f"sleeping at {net_connect.host}")
    time.sleep(5)

if __name__ == "__main__":
    all_devices = [nexus_site1, vyos1_site2, vyos2_site2]
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(connect_and_fetch, all_devices)
    end = time.time()
    print(end-start)

```

```text
cml@cml:~/python_automation$ python3 multithreading_netmiko.py 
172.16.14.210
*************
sleeping at 172.16.14.210
172.16.14.215
*************
sleeping at 172.16.14.215
172.16.14.216
*************
sleeping at 172.16.14.216
26.989115715026855
cml@cml:~/python_automation$ 
```

Let's increase the max_workers to 3 which is the total number of devices we have to see the impact of this change
Observe the difference in the time it takes to complete 3 devices in paralle now

```text
cml@cml:~/python_automation$ python3 multithreading_netmiko.py 
172.16.14.210
*************
sleeping at 172.16.14.210
172.16.14.215
*************
sleeping at 172.16.14.215
172.16.14.216
*************
sleeping at 172.16.14.216
9.750997304916382
```
