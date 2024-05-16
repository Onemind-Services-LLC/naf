## Exercise:
### Problem Statement:
In the previous task, we created an inventory of devices. Now, we need to use Ansible to ping all the devices in the inventory and check their status. Make sure to use the Docker environment created earlier for your development.

### Solution:

1. Open the terminal.

![alt text](image-25.png)

2. Run the container with the appropriate bind mount using the following command:

```sh
docker container run -it -v $(pwd):/ansible_automation ansible_lab
```

![alt text](image-8.png)

3. Navigate to the `/ansible_automation` directory within the container:

```sh
cd ansible_automation
```

![alt text](image-9.png)

4. Run the following command to ping all devices using an INI inventory:

```sh
ansible -m ping all -i inventory.ini 
```

![alt text](image-10.png)

Alternatively, you can use a YAML inventory with the following command:

```sh
ansible -m ping all -i inventory.yaml 
```

![alt text](image-13.png)