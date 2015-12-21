#/usr/bin/python

import textfsm

with open('output2.log') as f:
    raw_data = f.read()

template = open('cisco_show_ip_bgp.tmpl')
re_table = textfsm.TextFSM(template)

results = re_table.ParseText(raw_data)

with open('prefixes2.txt','w') as f:
    for row in results:
        f.write(row[1])
        f.write('\n')
