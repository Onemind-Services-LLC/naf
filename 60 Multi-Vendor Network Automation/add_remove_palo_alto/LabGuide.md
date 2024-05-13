# Adding removing firewall policy: PALO ALTO configuration

### Problem Statement:
* Need to add/remove the policy in palo alto firewall with ansible script

### Solution
* We will create ansible script to add firewall rule to block traffic between source 1.1.1.1 and destination 2.2.2.2.

## Lab guide:
### Creating inventory
1. Create new file inventor.ini add below content.

```inventory
[ny]
pa-site1        ansible_host=172.16.14.212  ansible_user=admin  ansible_password=Test12345 ansible_network_os=panos ansible_connection=local

[sf]
pa-site2        ansible_host=172.16.14.213  ansible_user=admin  ansible_password=Test12345 ansible_network_os=panos ansible_connection=local

[all:vars]
ansible_connection=ansible.netcommon.network_cli
ansible_user=admin
ansible_password=admin
ansible_become=true
ansible_become_method=enable
ansible_become_password=admin
```

2. Create new file with add_block_rule.yml and add below content.
```ansible
---
- name: Create block policy
  hosts: ny
  gather_facts: no
  vars:
    provider:
      ip_address: "172.16.14.212"
      username: "admin"
      password: "Test12345"

  tasks:
    - name: Add inbound rule to Panorama device group
      paloaltonetworks.panos.panos_security_rule:
        provider: '{{ provider }}'
        rule_name: 'block'
        description: 'block rule'
        source_zone: ['any']
        source_ip: ['1.1.1.1']
        destination_zone: ['any']
        destination_ip: ['2.2.2.2']
        action: 'deny'
        location: 'top'
        commit: 'true'
```
3. Verify the current connectivity status.

        >login to eveng server.
        > login to nxos device. Run below command

     ping 2.2.2.2 source 1.1.1.1
 shoud be able to ping from source to destination.

4. We need to run below command to execute ansible playbook
ansible-playbook add_block_rule.yml -i inventory.ini

5. Verify the connectivity again
  >login to eveng server.
        > login to nxos device. Run below command

     ping 2.2.2.2 source 1.1.1.1
shoud not be able to ping from source to destination.

We have added the policy successfully. We can verify the added policy in palo alto web interface.

## Removing the block policy.

1. Open VScode and create new file remove_block_rule.yml.

2. Add below code to remove_block_rule.yml file.

```ansible
---
- name: Create block policy
  hosts: ny
  gather_facts: no
  vars:
    provider:
      ip_address: "172.16.14.212"
      username: "admin"
      password: "Test12345"

  tasks:
    - name: Remove SSH inbound rule to Panorama device group
      paloaltonetworks.panos.panos_security_rule:
        provider: '{{ provider }}'
        state: 'absent'
        rule_name: 'block'
        commit: 'true'

```
3. Verify the current connectivity status.

        >login to eveng server.
        > login to nxos device. Run below command

     ping 2.2.2.2 source 1.1.1.1
 shoud be able to ping from source to destination.

 4. We need to run below command to execute ansible playbook
ansible-playbook remove_block_policy.yml -i inventory.ini

5. Verify the connectivity again
        >login to eveng server.
        > login to nxos device. Run below command

     ping 2.2.2.2 source 1.1.1.1
shoud be able to ping from source to destination.
