#!/usr/bin/python

import textfsm


with open('junos_l3_defip.txt') as f:
    data = f.read()

template = open('junos_l3_defip.tmpl')
re_table = textfsm.TextFSM(template)

results = re_table.ParseText(data)

for item in results:
    print 'Prefix: {}	ECMP Group: {}'.format(item[0],item[1])
