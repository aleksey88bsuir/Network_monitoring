import asyncio
import platform
import subprocess
from datetime import datetime
from loger import app_loger, log_exceptions


@log_exceptions(logger=app_loger)
async def ping_host(host_ip_add):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    process = await asyncio.create_subprocess_exec('ping', param,
                                                   '3', host_ip_add,
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE
                                                   )
    stdout, stderr = await process.communicate()
    return stdout.decode(), stderr.decode()


@log_exceptions(logger=app_loger)
async def monitor(hosts):
    tasks = [ping_host(host[1]) for host in hosts]
    result = await asyncio.gather(*tasks)
    exit_res = ''
    for host, res in zip(hosts, result):
        result_ = (f'Ping results for {host[1]} with id={host[0]}:'
                   f'\n{res}\nend_res\n')
        exit_res += result_
    return exit_res


if __name__ == '__main__':
    info_hosts = [
        (1, 'onliner.by'), (2, 'google.by'), (3, 'yandex.by'),
        (4, 'deal.by'), (5, 'talks.by'), (6, 'yandex.ru'),
        (7, 'mail.ru'), (8, 'google.com'), (9, 'narod.ru'),
        (10, 'ok.ru'), (11, 'bobr.by'), (12, 'kinopoisk.ru'),
        (13, 'sports.ru'), (14, 'kp.ru'), (15, '127.0.0.6')
    ]
    start = datetime.now()
    print(asyncio.run(monitor(info_hosts)))
    finish = datetime.now()
    print(finish-start)
