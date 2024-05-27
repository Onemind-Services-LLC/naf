## Exercise:
### Problem Statement:
Implement Jinja2 inheritence to create a familiar looking router configuration.  
If you look at the running configuration of a device, it is mostly broken down into subsections.  

```text
Building configuration...
!
hostname <>
!
vrf config
!
AAA config 
!
netflow config
!
object groups / acls
!
usernames
!
ipsec config
!
interface running config
!
routing configuration
!
nat
!
static routes
!
route-maps
!
snmp
!
tacacs
!
banners
!
line vty
!
```

### Solution

The idea is that the configuration itself is modular. Now if you were given the task of writing a jinja2 template for the entire running configuration for a site at initial deployment, it might be extremely complicated to pack in the entire running configuration into a single template file. It will probably be much easier to divide the template into smaller sub-sections which can then be imported into a single main template file.

```j2
#simplified running config in final_configuration template

{% include 'common.j2' %}
{% include 'aaa.j2' %}
{% include 'interfaces.j2' %}
{% include 'ospf.j2' %}
{% include 'bgp.j2' %}
```

Let's create all of the above jinja2 template files inside a templates directory and place the above content into a file named final_config.j2. The end result should look like this

![alt text](assets\image-20.png)

### common.j2
```jinja2
service tcp-keepalives-in
service tcp-keepalives-out
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
service password-encryption
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
!
hostname {{hostname}}
!
security authentication failure rate 3 log
security passwords min-length 8
logging buffered 16384
no logging console
enable secret {{enable_secret}}
!
ip domain name {{domain_name}}
!
```

### aaa.j2
```jinja2

aaa new-model
!
aaa group server tacacs+ {{tacacs_group}}
{% for server in server_name %}
 server name {{server}}
{% endfor %}
!
aaa authentication login default group TACACS_GROUP local
aaa authentication enable default group TACACS_GROUP enable
aaa authorization console
aaa authorization config-commands
aaa authorization exec default group TACACS_GROUP if-authenticated 
aaa authorization commands 15 default group TACACS_GROUP none 
aaa accounting exec default start-stop group TACACS_GROUP
aaa accounting commands 0 default start-stop group TACACS_GROUP
aaa accounting commands 1 default start-stop group TACACS_GROUP
aaa accounting commands 2 default start-stop group TACACS_GROUP
aaa accounting commands 5 default start-stop group TACACS_GROUP
aaa accounting commands 15 default start-stop group TACACS_GROUP
aaa accounting network default start-stop group TACACS_GROUP
aaa accounting connection default start-stop group TACACS_GROUP
aaa accounting system default start-stop group TACACS_GROUP
!
```
### interfaces.j2
```jinja2
{% for interface in interfaces %}
interface {{interface.number}}
 description {{interface.description}}
 bandwidth 10000
 ip address {{interface.ip}} {{interface.mask}}
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 media-type rj45
 speed 1000
 no negotiation auto
!
{% endfor %}
```
### ospf.j2
```jinja2
{% for ospf in ospf.ospf_processes %}
router ospf {{ospf.process_id}}
 router-id {{ospf.router_id}}
 area 0 authentication message-digest
 {% for network in ospf.network_id %}
 network {{network}}
 {% endfor %}
!
{% endfor %}
```
### bgp.j2
```jinja2
router bgp {{bgp.local_as}}
 bgp router-id {{bgp.router_id}}
 bgp log-neighbor-changes
 {% for peer_group in bgp.peer_groups %}
 neighbor {{peer_group.name}} peer-group
 neighbor {{peer_group.name}} remote-as 65001
 neighbor {{peer_group.name}} password 7 cisco
 neighbor {{peer_group.name}} update-source loopback0
 neighbor {{peer_group.name}} timers 15 45
 neighbor {{peer_group.name}} next-hop-self
 neighbor {{peer_group.name}} send-community both
 neighbor {{peer_group.name}} soft-reconfiguration inbound
 neighbor {{peer_group.name}} route-map FROM-{{peer_group.name}} in
 {% for ip in peer_group.neighbor_ip %}
 neighbor {{ip}} peer-group {{peer_group.name}}
 {% endfor %}
!
{% endfor %}
```
### final_config.j2
```jinja2
{% include 'common.j2' %}
{% include 'aaa.j2' %}
{% include 'interfaces.j2' %}
{% include 'ospf.j2' %}
{% include 'bgp.j2' %}
```

- Create a variables.yaml file

```yaml
# YAML variables.yaml
hostname: 'rtr-001-ce01'
enable_secret: cisco
domain_name: cisco.com
tacacs_group: 'TACACS_GROUP'

server_name: ['TACACS_1', 'TACACS_2', 'TACACS_3']
interfaces:
  -
    number: 'GigabitEthernet 0/1'
    description: 'WAN INTERFACE1'
    ip: 10.10.10.1
    mask: 255.255.255.0
    state: 'no shut'
  -
    number: 'GigabitEthernet 0/2'
    description: 'WAN INTERFACE2'
    ip: 10.10.20.1
    mask: 255.255.255.0
    state: 'no shut'
  -
    number: 'GigabitEthernet 1/0'
    description: 'LAN INTERFACE1'
    ip: 10.10.30.1
    mask: 255.255.255.0
    state: 'no shut'

ospf:
  ospf_processes:
    -
      process_id: 1
      router_id: 1.1.1.1
      network_id: 
        - 10.10.10.1 0.0.0.0 area 0
        - 10.10.20.1 0.0.0.0 area 0
        - 10.10.30.1 0.0.0.0 area 1

bgp:
  local_as: 65000
  router_id: 1.1.1.1
  peer_groups:
    -
      name: RR
      remote_as: 65001
      password: cisco
      update_source: loopback0
      route_map: FROM-RR
      neighbor_ip:
        - 11.11.11.1
        - 13.13.13.1
    -
      name: EBGP-PEER
      remote_as: 65002
      password: cisco
      update_source: loopback0
      route_map: FROM-RR
      neighbor_ip:
        - 100.100.100.1

```

- Putting it all together
- Create a python file named j2_to_yaml.py

```py
import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./templates'), lstrip_blocks=True, trim_blocks=True)
template = env.get_template('final_config.j2')
data = yaml.load(open('variables.yaml'), Loader=yaml.FullLoader)
print(template.render(data))
```
- The final output should look like below

```text
service tcp-keepalives-in
service tcp-keepalives-out
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
service password-encryption
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
!
hostname rtr-001-ce01
!
security authentication failure rate 3 log
security passwords min-length 8
logging buffered 16384
no logging console
enable secret cisco
!
ip domain name cisco.com
!
aaa new-model
!
aaa group server tacacs+ TACACS_GROUP
 server name TACACS_1
 server name TACACS_2
 server name TACACS_3
!
aaa authentication login default group TACACS_GROUP local
aaa authentication enable default group TACACS_GROUP enable
aaa authorization console
aaa authorization config-commands
aaa authorization exec default group TACACS_GROUP if-authenticated 
aaa authorization commands 15 default group TACACS_GROUP none 
aaa accounting exec default start-stop group TACACS_GROUP
aaa accounting commands 0 default start-stop group TACACS_GROUP
aaa accounting commands 1 default start-stop group TACACS_GROUP
aaa accounting commands 2 default start-stop group TACACS_GROUP
aaa accounting commands 5 default start-stop group TACACS_GROUP
aaa accounting commands 15 default start-stop group TACACS_GROUP
aaa accounting network default start-stop group TACACS_GROUP
aaa accounting connection default start-stop group TACACS_GROUP
aaa accounting system default start-stop group TACACS_GROUP
!
interface GigabitEthernet 0/1
 description WAN INTERFACE1
 bandwidth 10000
 ip address 10.10.10.1 255.255.255.0
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 media-type rj45
 speed 1000
 no negotiation auto
!
interface GigabitEthernet 0/2
 description WAN INTERFACE2
 bandwidth 10000
 ip address 10.10.20.1 255.255.255.0
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 media-type rj45
 speed 1000
 no negotiation auto
!
interface GigabitEthernet 1/0
 description LAN INTERFACE1
 bandwidth 10000
 ip address 10.10.30.1 255.255.255.0
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 media-type rj45
 speed 1000
 no negotiation auto
!
router ospf 1
 router-id 1.1.1.1
 area 0 authentication message-digest
 network 10.10.10.1 0.0.0.0 area 0
 network 10.10.20.1 0.0.0.0 area 0
 network 10.10.30.1 0.0.0.0 area 1
!
router bgp 65000
 bgp router-id 1.1.1.1
 bgp log-neighbor-changes
 neighbor RR peer-group
 neighbor RR remote-as 65001
 neighbor RR password 7 cisco
 neighbor RR update-source loopback0
 neighbor RR timers 15 45
 neighbor RR next-hop-self
 neighbor RR send-community both
 neighbor RR soft-reconfiguration inbound
 neighbor RR route-map FROM-RR in
 neighbor 11.11.11.1 peer-group RR
 neighbor 13.13.13.1 peer-group RR
!
 neighbor EBGP-PEER peer-group
 neighbor EBGP-PEER remote-as 65001
 neighbor EBGP-PEER password 7 cisco
 neighbor EBGP-PEER update-source loopback0
 neighbor EBGP-PEER timers 15 45
 neighbor EBGP-PEER next-hop-self
 neighbor EBGP-PEER send-community both
 neighbor EBGP-PEER soft-reconfiguration inbound
 neighbor EBGP-PEER route-map FROM-EBGP-PEER in
 neighbor 100.100.100.1 peer-group EBGP-PEER
!
```
