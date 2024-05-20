# Write a playbook to parse output of commands
# SOLUTION:
- lets create playbook in your current working directory (that is `ansible_automation`)  create a file `parser.yaml` with the below content


```yaml
- name: Parse command output
  hosts: nexus-site1
  gather_facts: no
  tasks:
    - name: TextFSM Parser
      ansible.utils.cli_parse:
        command: show version
        parser:
          name: ansible.netcommon.ntc_templates
      register: parsed_data
    
    - debug:
        msg: "{{ parsed_data }}"
```

- The output of the above playbook will look like this which contains parsed as well as unparsed data

```text
root@5e9393be42b8:/python_automation# ansible-playbook -i inventory.ini parser.yaml 

PLAY [Parse command output] *************************************************************************************************************************************************************************************************

TASK [TextFSM Parser] *******************************************************************************************************************************************************************************************************
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
ok: [nexus-site1]

TASK [debug] ****************************************************************************************************************************************************************************************************************
ok: [nexus-site1] => {
    "msg": {
        "changed": false,
        "failed": false,
        "parsed": [
            {
                "boot_image": "bootflash:///nxos.9.3.6.bin",
                "hostname": "nexus-site1",
                "last_reboot_reason": "Unknown",
                "os": "9.3(6)",
                "platform": "C9500v",
                "serial": "9RLR3ECFOO6",
                "uptime": "0 day(s), 21 hour(s), 45 minute(s), 16 second(s)"
            }
        ],
        "stdout": "Cisco Nexus Operating System (NX-OS) Software\nTAC support: http://www.cisco.com/tac\nDocuments: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html\nCopyright (c) 2002-2020, Cisco Systems, Inc. All rights reserved.\nThe copyrights to certain works contained herein are owned by\nother third parties and are used and distributed under license.\nSome parts of this software are covered under the GNU Public\nLicense. A copy of the license is available at\nhttp://www.gnu.org/licenses/gpl.html.\n\nNexus 9000v is a demo version of the Nexus Operating System\n\nSoftware\n  BIOS: version \n NXOS: version 9.3(6)\n  BIOS compile time:  \n  NXOS image file is: bootflash:///nxos.9.3.6.bin\n  NXOS compile time:  11/9/2020 23:00:00 [11/10/2020 11:00:21]\n\n\nHardware\n  cisco Nexus9000 C9500v Chassis (\"Supervisor Module\")\n   with 7935696 kB of memory.\n  Processor Board ID 9RLR3ECFOO6\n\n  Device name: nexus-site1\n  bootflash:    4287040 kB\nKernel uptime is 0 day(s), 21 hour(s), 45 minute(s), 16 second(s)\n\nLast reset \n  Reason: Unknown\n  System version: \n  Service: \n\nplugin\n  Core Plugin, Ethernet Plugin\n\nActive Package(s):",
        "stdout_lines": [
            "Cisco Nexus Operating System (NX-OS) Software",
            "TAC support: http://www.cisco.com/tac",
            "Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html",
            "Copyright (c) 2002-2020, Cisco Systems, Inc. All rights reserved.",
            "The copyrights to certain works contained herein are owned by",
            "other third parties and are used and distributed under license.",
            "Some parts of this software are covered under the GNU Public",
            "License. A copy of the license is available at",
            "http://www.gnu.org/licenses/gpl.html.",
            "",
            "Nexus 9000v is a demo version of the Nexus Operating System",
            "",
            "Software",
            "  BIOS: version ",
            " NXOS: version 9.3(6)",
            "  BIOS compile time:  ",
            "  NXOS image file is: bootflash:///nxos.9.3.6.bin",
            "  NXOS compile time:  11/9/2020 23:00:00 [11/10/2020 11:00:21]",
            "",
            "",
            "Hardware",
            "  cisco Nexus9000 C9500v Chassis (\"Supervisor Module\")",
            "   with 7935696 kB of memory.",
            "  Processor Board ID 9RLR3ECFOO6",
            "",
            "  Device name: nexus-site1",
            "  bootflash:    4287040 kB",
            "Kernel uptime is 0 day(s), 21 hour(s), 45 minute(s), 16 second(s)",
            "",
            "Last reset ",
            "  Reason: Unknown",
            "  System version: ",
            "  Service: ",
            "",
            "plugin",
            "  Core Plugin, Ethernet Plugin",
            "",
            "Active Package(s):"
        ]
    }
}

PLAY RECAP ******************************************************************************************************************************************************************************************************************
nexus-site1                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

- We can filter through the output to gather the intended information
- Let's look at parsed data only

```yaml
- name: Parse command output
  hosts: nexus-site1
  gather_facts: no
  tasks:
    - name: TextFSM Parser
      ansible.utils.cli_parse:
        command: show version
        parser:
          name: ansible.netcommon.ntc_templates
      register: parsed_data
    
    - debug:
        msg: "{{ parsed_data.parsed }}"
```

```text
root@5e9393be42b8:/python_automation# ansible-playbook -i inventory.ini parser.yaml 

PLAY [Parse command output] ***********************************************************************************************************************************************************************************************************************

TASK [TextFSM Parser] *****************************************************************************************************************************************************************************************************************************
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
ok: [nexus-site1]

TASK [debug] **************************************************************************************************************************************************************************************************************************************
ok: [nexus-site1] => {
    "msg": [
        {
            "boot_image": "bootflash:///nxos.9.3.6.bin",
            "hostname": "nexus-site1",
            "last_reboot_reason": "Unknown",
            "os": "9.3(6)",
            "platform": "C9500v",
            "serial": "9RLR3ECFOO6",
            "uptime": "0 day(s), 21 hour(s), 47 minute(s), 48 second(s)"
        }
    ]
}

PLAY RECAP ****************************************************************************************************************************************************************************************************************************************
nexus-site1                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

- We need to extract version, platform and serial number fields from the above parsed data

```yaml
- name: Parse command output
  hosts: nexus-site1
  gather_facts: no
  tasks:
    - name: TextFSM Parser
      ansible.utils.cli_parse:
        command: show version
        parser:
          name: ansible.netcommon.ntc_templates
      register: parsed_data
  
    - debug:
        msg: 
          - 'version is {{parsed_data["parsed"][0]["os"] }}'
          - 'platform is {{parsed_data["parsed"][0]["platform"] }}'
          - 'serial is {{parsed_data["parsed"][0]["serial"] }}'
```

```text
root@5e9393be42b8:/python_automation# ansible-playbook -i inventory.ini parser.yaml 

PLAY [Parse command output] ***********************************************************************************************************************************************************************************************************************

TASK [TextFSM Parser] *****************************************************************************************************************************************************************************************************************************
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
ok: [nexus-site1]

TASK [debug] **************************************************************************************************************************************************************************************************************************************
ok: [nexus-site1] => {
    "msg": [
        {
            "boot_image": "bootflash:///nxos.9.3.6.bin",
            "hostname": "nexus-site1",
            "last_reboot_reason": "Unknown",
            "os": "9.3(6)",
            "platform": "C9500v",
            "serial": "9RLR3ECFOO6",
            "uptime": "0 day(s), 21 hour(s), 49 minute(s), 24 second(s)"
        }
    ]
}

TASK [debug] **************************************************************************************************************************************************************************************************************************************
ok: [nexus-site1] => {
    "msg": [
        "version is 9.3(6)",
        "platform is C9500v",
        "serial is 9RLR3ECFOO6"
    ]
}

PLAY RECAP ****************************************************************************************************************************************************************************************************************************************
nexus-site1                : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

- Let's parse the output of multiple commands
- Print only the parsed output
- Comment out of loop_control and label fields to see the difference it makes

```yaml
- name: Parse command output
  hosts: nexus-site1
  gather_facts: no
  tasks:
    - name: TextFSM Parser
      ansible.utils.cli_parse:
        command: "{{ item }}"
        parser:
          name: ansible.netcommon.ntc_templates
      register: parsed_data
      with_items:
        - "show version"
        - "show ip interface brief"

    - debug:
        msg: "{{ item.parsed }}"
      with_items: "{{ parsed_data.results }}"
      loop_control:
        label: "PARSED DATA"
```

```text
root@5e9393be42b8:/python_automation# ansible-playbook -i inventory.ini parser.yaml 

PLAY [Parse command output] ***********************************************************************************************************************************************************************************************************************

TASK [TextFSM Parser] *****************************************************************************************************************************************************************************************************************************
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
ok: [nexus-site1] => (item=show version)
ok: [nexus-site1] => (item=show ip interface brief)

TASK [debug] **************************************************************************************************************************************************************************************************************************************
ok: [nexus-site1] => (item=PARSED DATA) => {
    "msg": [
        {
            "boot_image": "bootflash:///nxos.9.3.6.bin",
            "hostname": "nexus-site1",
            "last_reboot_reason": "Unknown",
            "os": "9.3(6)",
            "platform": "C9500v",
            "serial": "9RLR3ECFOO6",
            "uptime": "0 day(s), 22 hour(s), 11 minute(s), 27 second(s)"
        }
    ]
}
ok: [nexus-site1] => (item=PARSED DATA) => {
    "msg": [
        {
            "interface": "Vlan10",
            "ip_address": "192.168.1.1",
            "link": "link-up",
            "proto": "protocol-up",
            "status": "admin-up",
            "vrf": "default"
        },
        {
            "interface": "Eth1/1",
            "ip_address": "10.10.10.2",
            "link": "link-up",
            "proto": "protocol-up",
            "status": "admin-up",
            "vrf": "default"
        },
        {
            "interface": "Eth1/3",
            "ip_address": "10.10.10.6",
            "link": "link-up",
            "proto": "protocol-up",
            "status": "admin-up",
            "vrf": "default"
        }
    ]
}

PLAY RECAP ****************************************************************************************************************************************************************************************************************************************
nexus-site1                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

root@5e9393be42b8:/python_automation# 
```
