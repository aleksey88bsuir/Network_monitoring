from queue import Queue
from threading import Thread
import time
import os
import sys
from network_monitoring import handle_info_about_host


sys.path.insert(0,
                os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


hosts = [('google.com', 'google.com'),
         ('onliner.by', 'onliner.by'),
         ('127.0.0.1', 'my_comp'),
         ('172.19.5.110', 'AAA'),
         ('10.10.15.101', 'BBB'),
         ('13.17.22.12', 'CCC'),
         ('19.156.187.23', 'DDD'),
         ('234.243.123.32', 'EEE')
         ]


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result_ = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} took {end_time - start_time}'
              f' seconds to execute.')
        return result_
    return wrapper


@timer_decorator
def check_available_all_hosts_with_threading():
    queue = Queue()
    threads = []
    for host in hosts:
        t = Thread(target=handle_info_about_host,
                   args=(host[0], host[1], queue))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    while not queue.empty():
        results.append(queue.get())
    return results


@timer_decorator
def check_available_all_hosts_without_threading():
    for host in hosts:
        print(handle_info_about_host(host_ip=host[0], host_name=host[1]))


if __name__ == "__main__":
    result = check_available_all_hosts_with_threading()
    for res in result:
        print(res)
    print('='*60)
    check_available_all_hosts_without_threading()
