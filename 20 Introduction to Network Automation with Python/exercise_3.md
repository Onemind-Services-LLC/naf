##  Exercise-3:
### Problem Statement:
Develop a Python program to check the status of a router by pinging its IP address. Your task is to utilize functions, control statements, exception handling, and module imports to create this program. Here are the requirements:

1. Write the program in Python.
2. Import necessary modules to enable functionality.
3. Define a function `check_router_status(router_ip)` to determine the online or offline status of the router.
4. Implement the main logic within the `main()` function:
    - Prompt the user to input the IP address of the router.
    - Use a loop to retry connectivity if the router is offline, with a maximum number of retries specified by the constant `MAX_RETRIES`.
    - Handle exceptions, including KeyboardInterrupt, to gracefully exit the program if needed.
5. Display appropriate messages to inform the user about the router's status and the outcome of the connection attempts.

Ensure that your program follows structured coding practices and effectively handles scenarios where the router may not be reachable or if the user interrupts the execution.


### Solution
```python
import os
import time

MAX_RETRIES = 5

def check_router_status(router_ip):
    response = os.system("ping -c 1 " + router_ip)  # Ping the router once
    if response == 0:
        return True  # Router is reachable
    else:
        return False  # Router is unreachable

def main():
    retry_count = 0
    while True:
        try:
            router_ip = input("Enter the IP address of your router: ")
            if check_router_status(router_ip):
                print("Router is online")
                break  # Exit the loop if router is online
            else:
                retry_count += 1
                print("Router is offline. Retrying...")
                if retry_count == MAX_RETRIES:
                    print("Router is not reachable after", MAX_RETRIES, "attempts.")
                    break
                time.sleep(1)  # Wait for 1 second before retrying
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()

```

In this program:
- We define a function `check_router_status()` that takes the IP address of the router as input and pings it once using the `ping` command. If the ping is successful (response code 0), it returns `True`; otherwise, it returns `False`.
- The `main()` function prompts the user to enter the IP address of the router, calls the `check_router_status()` function, and prints the appropriate message based on the router's status.
- The `if __name__ == "__main__":` block ensures that the `main()` function is executed when the script is run directly.

To use this program:
1. Save it to a Python file (e.g., `router_status_checker.py`).
2. Run the script, and it will prompt you to enter the IP address of your router.
3. After entering the IP address, the program will check if the router is online or offline and display the result accordingly.