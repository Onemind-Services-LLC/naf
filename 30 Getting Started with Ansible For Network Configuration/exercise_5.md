# Backup configuration of all devices


```yaml
---
- name: Backup configuration of devices in dc_group
  hosts:  vyos1-site2,vyos2-site2
  gather_facts: no
  tasks:
    - name: configurable backup path
      vyos.vyos.vyos_config:
        backup: yes
        backup_options:
          filename: {{ inventory_hostname }}.cfg
          dir_path: ./vyos_backups

   

```

### Execute the above playbook

```
ansible-playbook -i inventory.ini your_playbook.yml
```

Make sure the playbook file and the inventory file are in the same directory, or provide the correct path to the playbook file if it's in a different directory.

![alt text](image-33.png)

![alt text](image-34.png)