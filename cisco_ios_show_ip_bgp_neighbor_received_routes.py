#/usr/bin/python

import textfsm

with open('show_ip_bgp_neighbor_received_routes.txt') as f:
    raw_data = f.read()

template = open('cisco_show_ip_bgp.tmpl')
re_table = textfsm.TextFSM(template)

results = re_table.ParseText(raw_data)

for row in results:
    print row[1]
