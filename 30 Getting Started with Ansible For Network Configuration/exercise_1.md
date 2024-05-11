##  Exercise:
### Problem Statement:
### Create an Ansible inventory that includes the following hosts

| Device name  | Device Group |      IP         | username | password |
|--------------|--------------|-----------------|----------|----------|
| csr          | dc_group     | 172.16.14.110   | admin    | admin    |
| arista       | dc_group     | 172.16.14.111   | admin    | admin    |
| nxos_1       | dc_group     | 172.16.14.112   | admin    | admin    |
| nxos_2       | dc_group     | 172.16.14.113   | admin    | admin    |
| vios1        | sitea_group  | 172.16.14.114   | admin    | admin    |
| vyos1        | sitea_group  | 172.16.14.115   | admin    | admin    |
| vios2        | siteb_group  | 172.16.14.116   | admin    | admin    |
| vyos2        | siteb_group  | 172.16.14.117   | admin    | admin    |

For the host named "local_test," ensure it uses a local connection method. Additionally  
Organize the hosts into groups:

- dc_group,
- sitea_group
- siteb_group
- a nested group "branch" that includes "sitea" and "siteb" as children.
- Include variables such as "connection," "netbox_os," "username," "password," and "become_method" within the inventory.

### Solution
to do this exercise create a folder `ansible_automation` in user's home directory using
- in last excercise we were in containers shell to exit from there run the exit command
```sh
exit
```
![alt text](image.png)
- to create a ansible_automation directory in users home directory run the below commands
```sh
cd ~
mkdir ansible_automation
cd ansible_automation
```
![alt text](image-1.png)
open the vscode in newly created directory for that lets run the below command
```sh
code .
```
![alt text](image-2.png)
it will ask you the password for the user, when u give the password, it should open vscode in `ansible_automation` folder
![alt text](image-3.png)
lets create a new file with `inventory.ini` with below content
![alt text](image-4.png)
```ini
local_test ansible_connection=local

[ny]
nexus-site1     ansible_host=172.16.14.210  ansible_user=admin  ansible_password=admin ansible_network_os=eos
vmx1-site1      ansible_host=172.16.14.211  ansible_user=root   ansible_password=Juniper ansible_network_os=junos
pa-site1        ansible_host=172.16.14.212  ansible_user=admin  ansible_password=Test12345 ansible_network_os=panos ansible_connection=local

[sf]
pa-site2        ansible_host=172.16.14.213  ansible_user=admin  ansible_password=Test12345 ansible_network_os=panos ansible_connection=local
arista1-site2   ansible_host=172.16.14.214  ansible_user=admin  ansible_password=password ansible_network_os=eos
vyos1-site1     ansible_host=172.16.14.215  ansible_user=vyos   ansible_password=vyos ansible_network_os=vyos
vyos2-site2     ansible_host=172.16.14.216  ansible_user=vyos   ansible_password=vyos ansible_network_os=vyos

[all:vars]
ansible_connection=ansible.netcommon.network_cli
ansible_user=admin
ansible_password=admin
ansible_become=true
ansible_become_method=enable
ansible_become_password=admin

```
![alt text](image-5.png)

## YAML FORMAT

1. Create a file named inventory.yaml
2. Copy paste the below content in that file

```yaml
all:
  vars:
    ansible_connection: ansible.netcommon.network_cli
    ansible_user: admin
    ansible_password: admin
    ansible_become: true
    ansible_become_method: enable
    ansible_become_password: admin

ny:
  hosts:
    nexus-site1:
      ansible_host: 172.16.14.210
      ansible_user: admin
      ansible_password: admin
      ansible_network_os: eos
    vmx1-site1:
      ansible_host: 172.16.14.211
      ansible_user: root
      ansible_password: Junper
      ansible_network_os: junos
    pa-site1:
      ansible_host: 172.16.14.212
      ansible_user: admin
      ansible_password: Test12345
      ansible_network_os: panos
      ansible_connection: local

sf:
  hosts:
    pa-site2:
      ansible_host: 172.16.14.213
      ansible_user: admin
      ansible_password: Test12345
      ansible_network_os: panos
      ansible_connection: local
    arista1-site2:
      ansible_host: 172.16.14.214
      ansible_user: admin
      ansible_password: password
      ansible_network_os: eos
    vyos1-site1:
      ansible_host: 172.16.14.215
      ansible_user: vyos
      ansible_password: vyos
      ansible_network_os: vyos
    vyos2-site2:
      ansible_host: 172.16.14.216
      ansible_user: vyos
      ansible_password: vyos
      ansible_network_os: vyos

```
![alt text](image-14.png)