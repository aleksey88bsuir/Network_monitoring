from db.work_with_table_hosts import WorkWithHosts


data_list = [
    dict(ip_add='172.18.100.1', name='VLAN L3 SWITCH', music='', descr='',),
    dict(ip_add='172.18.100.177', name='IP_TLF', music='', descr='',),
    dict(ip_add='192.175.15.211', name='SIP-server', music='', descr='',),
    dict(ip_add='172.19.5.38', name='NKU', music='', descr='',),
    dict(ip_add='172.18.110.1', name='R-443O', music='', descr='',)
]

wwh = WorkWithHosts()

for host in data_list:
    wwh.create(host)

data = wwh.read_all_data()
for i in data:
    print(i.name, i.ip_add)

for i in data:
    wwh.delete_host(i)
