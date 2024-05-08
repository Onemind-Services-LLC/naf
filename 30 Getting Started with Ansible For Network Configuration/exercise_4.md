### Modify the previous playbook to save output of all commands in a single file

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

    - name: Concatenate show version and show IP interface brief outputs
      set_fact:
        combined_output: "{{ show_version_output.results[0].stdout[0] }}\n\n{{ show_version_output.results[0].stdout[1] }}"

    - name: Save combined output to file
      ansible.builtin.copy:
        content: "{{ combined_output }}"
        dest: "/path/to/save/{{ inventory_hostname }}_combined_output.txt"
```

### Execute the above playbook

```
ansible-playbook -i inventory.ini your_playbook.yml
```

Make sure the playbook file and the inventory file are in the same directory, or provide the correct path to the playbook file if it's in a different directory.
