#/usr/bin/python

import textfsm

with open('junos_lldp_neighbors.txt') as f:
    raw_data = f.read()

template = open('junos_show_lldp_neighbors.tmpl')
re_table = textfsm.TextFSM(template)

results = re_table.ParseText(raw_data)

new_list = []
order = [2,0,1]
for item in results:
    item = [item[i] for i in order]
    new_list.append(item)

print new_list
