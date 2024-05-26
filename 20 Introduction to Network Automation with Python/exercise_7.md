## Exercise:
### Problem Statement:
Use a jinja2 template to create the below configuration from a YAML source file

```text
hostname my-rtr-01
!
interface Loopback0
  ip address 1.1.1.1 255.255.255.255
!
vlan 10
  name data
!
vlan 20
  name voice
!
vlan 30
  name mgmt
!
router ospf 1
  router-id 1.1.1.1
  auto-cost reference-bandwidth 10000
  network 10.10.10.0 0.0.0.255 area 0
  network 10.10.20.0 0.0.0.255 area 0
  network 10.10.30.0 0.0.0.255 area 1
```

### Solution
- Create a python file with name 'source.yaml'

```yaml
---

hostname: my-rtr-01
loopback: 1.1.1.1 255.255.255.255
vlans:
  10: data
  20: voice
  30: mgmt
ospf:
  - subnet: 10.10.10.0 0.0.0.255
    area: 0
  - subnet: 10.10.20.0 0.0.0.255
    area: 0
  - subnet: 10.10.30.0 0.0.0.255
    area: 1
```

- Create a python file with name 'j2_to_config.py'

```py
import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader

variable_data = yaml.load(open('source.yaml'), Loader=yaml.FullLoader)
print(variable_data)
```
```text
{
    'hostname': 'my-rtr-01',
    'loopback': '1.1.1.1 255.255.255.255',
    'vlans': {10: 'data', 20: 'voice', 30: 'mgmt'},
    'ospf': [{'subnet': '10.10.10.0 0.0.0.255', 'area': 0}, {'subnet': '10.10.20.0 0.0.0.255', 'area': 0}, {'subnet': '10.10.30.0 0.0.0.255', 'area': 1}]
}
```

Now we need a template that can subsite the values that the python script has read from the YAML file. While reading the below j2 template, keep in mind the end configuration that we want to generate.

- {{ }} variable name inside these brackets is the variable name inside the yaml file.
- Each key-value pair in yaml is read as a dictionary by python while loading yaml.
- Key values denoted by ‘ — ‘ are regarded as elements of the same list. So ospf key contains a list of dictionaries

- Create a j2 template file named j2template.j2

```j2
hostname {{ hostname }}
!
interface Loopback0
 ip address {{ loopback }}
!
{% for vlan, name in vlans.items() %}
vlan {{ vlan }}
 name {{ name }}
! 
{% endfor %}
router ospf 1
 auto-cost reference-bandwidth 10000
 {% for networks in ospf %}
 network {{ networks.network }} area {{ networks.area }}
 {% endfor %}
!
```

- Modify the python script to below

```py
import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader

variable_data = yaml.load(open('source.yaml'), Loader=yaml.FullLoader)
print(variable_data)

env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('template.j2')
print(template)
print(template.render(variable_data))

```
Your output should look like this or similar to this

```output
{
    'hostname': 'my-rtr-01',
    'loopback': '1.1.1.1 255.255.255.255',
    'vlans': {10: 'data', 20: 'voice', 30: 'mgmt'},
    'ospf': [{'subnet': '10.10.10.0 0.0.0.255', 'area': 0}, {'subnet': '10.10.20.0 0.0.0.255', 'area': 0}, {'subnet': '10.10.30.0 0.0.0.255', 'area': 1}]
}
<Template 'j2template.j2'>
hostname my-rtr-01
!
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
vlan 10
 name data
! 
vlan 20
 name voice
! 
vlan 30
 name mgmt
! 
router ospf 1
 auto-cost reference-bandwidth 10000
 network  area 0
 network  area 0
 network  area 1
!
```
