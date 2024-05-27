# OBJECTIVE:
### Modify the previous playbook to save output of all commands in a single file

# SOLUTION:
- lets create playbook in your current working directory (that is `ansible_automation`)  create a file `multi_cmnd_single.yaml` with the below content

```yaml
---
- name: Fetch show version from devices in sf
  hosts: vyos1-site2,vyos2-site2
  gather_facts: no
  tasks:
    - name: Create Config directory
      run_once: true
      ansible.builtin.file:
        path: "./multi_cmd_single/"
        state: directory

    - name: Run show version command
      register: show_version_output
      vyos_command:
        commands:
          - show version
          - show interfaces
    
    - name: Concatenate show version and show IP interface brief outputs
      set_fact:
        combined_output: "{{ show_version_output.stdout[0] }}\n\n{{ show_version_output.stdout[1] }}"

    - name: Save combined output to file
      ansible.builtin.copy:
        content: "{{ combined_output | replace('\\n','\n') }}"
        dest: "./multi_cmd_single/{{ inventory_hostname }}_combined_output.txt"


```

### Execute the above playbook

```
ansible-playbook -i inventory.ini multi_cmnd_single.yaml
```

![alt text](assets\image-31.png)

Make sure the playbook file and the inventory file are in the same directory, or provide the correct path to the playbook file if it's in a different directory.

![alt text](assets\image-32.png)