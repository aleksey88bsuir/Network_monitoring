import re
from async_net_monitoring import monitor
import asyncio


def respond_query_data_and_transform(hosts):
    ping_results_string = asyncio.run(monitor(hosts))
    string_list_hosts_info = ping_results_string.split('end_res')
    host_data_list = list()
    for string_host_info in string_list_hosts_info[:-1]:
        ip_add_pattern = r'Ping results for (\S+) with'
        id_pattern = r'Ping results for \S+ with id=(\d+):'
        # head_pattern = r'Ping results for (\S+) with id=(\d+):'
        transmitted_pattern = r'(\d+) packets transmitted'
        received_pattern = r'(\d+) received'
        average_delay_pattern = r'min/avg/max/mdev = (\d+\.\d+)/(\d+\.\d+)/'
        # min/avg/max/mdev = 0.019/0.029/0.038/0.007
        ip_add = re.findall(ip_add_pattern, string_host_info)[0]
        id_ = re.findall(id_pattern, string_host_info)[0]
        transmitted_packets = re.findall(transmitted_pattern, string_host_info)
        received_packets = re.findall(received_pattern, string_host_info)
        average_delay_ = re.findall(average_delay_pattern, string_host_info)
        transmitted_packets = int(transmitted_packets[0]) if (
            transmitted_packets) else 0
        received_packets = int(received_packets[0]) if received_packets else 0
        avg_delay = round(float(average_delay_[0][1]), 4) if average_delay_ \
            else None
        dict_host_info = {
            'id': int(id_),
            'ip': ip_add,
            'packets transmitted': transmitted_packets,
            'packets received': received_packets,
            'avg': avg_delay,
        }
        host_data_list.append(dict_host_info)
    return host_data_list


def allocation_to_lists_async(hosts):
    host_data_list = respond_query_data_and_transform(hosts)
    online_lists = []
    online_lists_with_error = []
    offline_lists = []
    for host in host_data_list:
        id_ = host.get('id')
        ip_add = host.get('ip')
        tx_pac = host.get('packets transmitted')
        rx_pac = host.get('packets received')
        avg = host.get('avg')
        if avg is None:
            offline_lists.append((id_, ip_add))
        elif tx_pac == 3 and rx_pac == 3:
            online_lists.append((id_, ip_add, avg))
        else:
            lost_pac = tx_pac - rx_pac
            online_lists_with_error.append((id_, ip_add, avg, lost_pac))
    return online_lists, online_lists_with_error, offline_lists


if __name__ == "__main__":
    info_hosts = [(1, 'onliner.by'), (2, 'google.by'),
                  (3, 'yandex.by'), (4, 'deal.by'),
                  (5, 'talks.by'), (6, 'yandex.ru'),
                  (7, 'mail.ru'), (8, 'google.com'),
                  (9, 'narod.ru'), (10, 'ok.ru'),
                  (11, 'bobr.by'), (12, 'kinopoisk.ru'),
                  (13, 'sports.ru'), (14, 'kp.ru'),
                  (15, '127.0.0.6')
                  ]
    for _ in range(10):
        for response in respond_query_data_and_transform(info_hosts):
            print(response)
