import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.1.233', 'jbc', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_arp_table()
print (json.dumps(ios_output, indent=4))

