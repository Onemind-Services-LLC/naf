### Write a filter plugin that replaces underscore with space and coverts the string into TitleCase

To create a custom Ansible filter plugin to convert a MAC address from `XX:XX:XX:XX:XX:XX` format to `XXXX.XXXX.XXXX` format, you can follow these steps:

1. Create a new directory for your custom filter plugin. Let's name it `filter_plugins`.
2. Inside the `filter_plugins` directory, create a Python file for your filter plugin. Let's name it `mac_format.py`.
3. Open `mac_format.py` and define your custom filter plugin.

Here's how you can implement the custom filter plugin:

```python
# filter_plugins/mac_format.py

class FilterModule(object):
    def filters(self):
        return {
            'format_mac': self.format_mac,
        }

    def format_mac(self, mac_address):
        # Remove colons from the MAC address
        mac_address = mac_address.replace(':', '')

        # Insert dots between every 4 characters
        formatted_mac = '.'.join(mac_address[i:i+4] for i in range(0, len(mac_address), 4))

        return formatted_mac
```

Save the file, and now you can use the `format_mac` filter in your Ansible playbooks or templates.

Here's how you can use it in a playbook:

```yaml
---
- name: Example playbook using custom filter plugin
  hosts: localhost
  vars:
    mac_address: "01:23:45:67:89:AB"
  tasks:
    - debug:
        msg: "Formatted MAC address: {{ mac_address | format_mac }}"
```

When you run the playbook, it will output:

```
TASK [debug] *******************************************************************
ok: [localhost] => {
    "msg": "Formatted MAC address: 0123.4567.89AB"
}
```

The custom filter plugin `format_mac` converts the MAC address from `01:23:45:67:89:AB` format to `0123.4567.89AB` format as expected.
