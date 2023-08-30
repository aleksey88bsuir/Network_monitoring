from db.work_with_table_hosts import WorkWithHosts
from db.work_with_table_lp import WorkWithLostPackets
from db.work_with_table_inf_host import WorkWithHostStatus


data_list = [
    dict(ip_add='onliner.by', name='VLAN L3 SWITCH', music='', descr='',),
    dict(ip_add='google.by', name='SIP-server', music='', descr='',),
    dict(ip_add='yandex.by', name='NKU', music='', descr='',),
    dict(ip_add='deal.by', name='R-443O', music='', descr='',),
    dict(ip_add='talks.by', name='R-4432', music='', descr='',),
    dict(ip_add='yandex.ru', name='R-4434', music='', descr='',),
    dict(ip_add='mail.ru', name='R-4435', music='', descr='',),
    dict(ip_add='google.com', name='R-4437', music='', descr='',),
    dict(ip_add='narod.ru', name='R-4438', music='', descr='',),
    dict(ip_add='ok.ru', name='R-44312', music='', descr='',),
    dict(ip_add='bobr.by', name='R-44314', music='', descr='',),
    dict(ip_add='kinopoisk.ru', name='R-44316', music='', descr='',),
    dict(ip_add='sports.ru', name='R-44318', music='', descr='',),
    dict(ip_add='kp.ru', name='R-44319', music='', descr='',),
    dict(ip_add='127.0.0.6', name='R-44321', music='', descr='',),
]


def start_test_table_host():
    wwh = WorkWithHosts()

    for host in data_list:
        wwh.create(host)


def start_test_with_table_lost_packets():
    wwlp = WorkWithLostPackets()
    wwlp.create(1, 1)
    wwlp.create(2, 2)
    wwlp.create(1, 2)


def start_test_with_table_inf_about_hosts():
    wwhs = WorkWithHostStatus()
    wwhs.create(1, 'online')
    wwhs.create(2, 'online')
    wwhs.create(1, 'offline')


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
    # start_test_table_host()
    # start_test_with_table_lost_packets()
    # start_test_with_table_inf_about_hosts()
    check_work_cascade_delete()
