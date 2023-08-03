from db.work_with_table_hosts import WorkWithHosts
from db.work_with_table_lp import WorkWithLostPackets
from db.work_with_table_inf_host import WorkWithHostStatus


data_list = [
    dict(ip_add='172.18.100.1', name='VLAN L3 SWITCH', music='', descr='',),
    dict(ip_add='172.18.100.177', name='IP_TLF', music='', descr='',),
    dict(ip_add='192.175.15.211', name='SIP-server', music='', descr='',),
    dict(ip_add='172.19.5.38', name='NKU', music='', descr='',),
    dict(ip_add='172.18.110.1', name='R-443O', music='', descr='',)
]


def start_test_table_host():
    wwh = WorkWithHosts()

    for host in data_list:
        wwh.create(host)

    update_host = None
    data = wwh.read_all_data()
    for k, i in enumerate(data):
        print(i.name, i.ip_add)
        if k == 2:
            update_host = i

    update_host.name = 'New_SIP_server'
    update_host.ip_add = '192.175.15.212'
    update_host.descr = 'AAA'
    update_host.music = 'misic_file'

    wwh.update_host(update_host)

    # data = wwh.read_all_data()
    # for k, i in enumerate(data):
    #     print(i.name, i.ip_add)
    #
    # print('++'*30)
    # print(wwh.read_info_about_host(2))

    # for i in data:
    #     wwh.delete_host(i)


def start_test_with_table_lost_packets():
    wwlp = WorkWithLostPackets()
    wwlp.create(1, 1)
    wwlp.create(2, 2)
    wwlp.create(1, 2)
    # for i in wwlp.read_all_data():
    #     print(i)
    #     print('-'*30)
    # print(wwlp.read_info_about_host(1))
    # print(wwlp.read_info_about_host(2))


def start_test_with_table_inf_about_hosts():
    wwhs = WorkWithHostStatus()
    wwhs.create(1, 'online')
    wwhs.create(2, 'online')
    wwhs.create(1, 'offline')
    # for i in wwhs.read_all_data():
    #     print(i)
    #     print('-'*30)
    # print(wwhs.read_info_about_host(1))
    # print(wwhs.read_info_about_host(2))
    #


def check_work_cascade_delete():
    wwh = WorkWithHosts()
    data = wwh.read_all_data()
    if data:
        start_test_with_table_inf_about_hosts()
        start_test_with_table_lost_packets()
        wwhs = WorkWithHostStatus()
        assert len(wwhs.read_all_data()) > 0
        wwlp = WorkWithLostPackets()
        assert len(wwlp.read_all_data()) > 0
        for i in data:
            wwh.delete_host(i)
        wwhs = WorkWithHostStatus()
        assert len(wwhs.read_all_data()) == 0
        wwlp = WorkWithLostPackets()
        assert len(wwlp.read_all_data()) == 0


if __name__ == "__main__":
    start_test_table_host()
    start_test_with_table_lost_packets()
    start_test_with_table_inf_about_hosts()
    check_work_cascade_delete()
