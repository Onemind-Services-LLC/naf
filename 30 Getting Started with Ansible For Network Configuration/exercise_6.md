# Parse command outputs with Ansible using Pyats

- name: "Run command and parse with pyats"
  ansible.utils.cli_parse:
    command: show interface
    parser:
      name: ansible.netcommon.pyats
    set_fact: interfaces