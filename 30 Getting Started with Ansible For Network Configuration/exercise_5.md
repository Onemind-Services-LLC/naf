# Backup configuration of all devices


```yaml
---
- name: Backup configuration of devices in dc_group
  hosts: dc_group
  gather_facts: no
  tasks:
    - name: Determine device type
      set_fact:
        device_type: "cisco"
      when: inventory_hostname != "arista"

    - name: Determine device type (Arista)
      set_fact:
        device_type: "arista"
      when: inventory_hostname == "arista"

    - name: Backup configuration (Cisco)
      when: device_type == "cisco"
      ios_config:
        backup: yes
      register: config_backup

    - name: Backup configuration (Arista)
      when: device_type == "arista"
      arista.eos_config:
        backup: yes
      register: config_backup

    - name: Save configuration backup to file
      ansible.builtin.copy:
        content: "{{ config_backup.backup }}"
        dest: "/path/to/save/{{ inventory_hostname }}_config_backup.txt"

```

### Execute the above playbook

```
ansible-playbook -i inventory.ini your_playbook.yml
```

Make sure the playbook file and the inventory file are in the same directory, or provide the correct path to the playbook file if it's in a different directory.
