### Modify the previous playbook to run multple commands

```yaml
---
- name: Fetch show version and show IP interface brief from devices in dc_group
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

    - name: Run show version command
      when: device_type == "cisco"
      ios_command:
        commands:
          - show version
          - show ip interface brief
      register: show_version_output

    - name: Run show version and show IP interface brief commands (Arista)
      when: device_type == "arista"
      arista.eos_command:
        commands:
          - show version
          - show ip interface brief
      register: show_version_output

    - name: Save show version output to file
      ansible.builtin.copy:
        content: "{{ item.stdout[0] }}"
        dest: "/path/to/save/{{ inventory_hostname }}_show_version.txt"
      loop: "{{ show_version_output.results }}"

    - name: Save show IP interface brief output to file
      ansible.builtin.copy:
        content: "{{ item.stdout[1] }}"
        dest: "/path/to/save/{{ inventory_hostname }}_show_ip_interface_brief.txt"
      loop: "{{ show_version_output.results }}"

```

### Execute the above playbook

```
ansible-playbook -i inventory.ini your_playbook.yml
```

Make sure the playbook file and the inventory file are in the same directory, or provide the correct path to the playbook file if it's in a different directory.
