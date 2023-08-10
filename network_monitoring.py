from ping3 import ping
from time import sleep


data = [
        [0.05846047401428223, 0.08408832550048828, 0.061429738998413086],
        [0.09540486335754395, 0.08738088607788086, 0.08862137794494629],
        [0.05481839179992676, 0.05638599395751953, 0.05617809295654297],
        [0.0003616809844970703, 0.00034046173095703125, 0.0003154277801513672],
        [None, 0.48400211334228516, 0.061843156814575195],
    ]

def __check_host(host_ip: str) -> tuple:
    """
    Функция посылает 3 icmp пакета для проверки качества линии связи,
    используя функцию ping. Функция ping возвращает: float - OK (среднее
    время задержки), False - хост недоступен, None - ошибка в сети
    :param host_ip: ip адрес хоста
    :return: Результат 3-х ping запросов в виде кортежа
    """
    result = []
    for i in range(3):
        sleep(.2)
        result.append(ping(host_ip))
    # print(result)
    return tuple(result)


def handle_info_about_host(host_name: str, host_ip: str,
                           queue=None) -> tuple:
    """
    Обрабатывает информацию, полученную от check_host
    :param host_ip: ip адрес хоста
    :param host_name: доменное имя хоста (узла связи)
    :param queue: Объект класса Queue. Необходим для работы в многопоточном
    режиме
    :return: возвращает результат обработки информации, полученной от хоста
    в виде кортежа
    execution_code = -1: произошла непредвиденная ошибка
    execution_code = 0: запрашиваемый узел доступен, пингуется без ошибок
    execution_code = 1: Присутствуют ошибки при пинге запрашиваемого узла
    execution_code = 2: запрашиваемый узел недоступен
    """
    try:
        info = __check_host(host_ip)
        # if all(info) is None:
        if info[0] is None and info[1] is None and info[2] is None:
        # if all(i) is None:
            execution_code = -1
            result = execution_code, host_name, host_ip
            if queue:
                queue.put(result)
            # print('Error')
            return result

        if info[0] is False and info[1] is False and info[2] is False:
        # if i[0] is False and i[1] is False and i[2] is False:
            execution_code = 2
            result = execution_code, host_name, host_ip
            if queue:
                queue.put(result)
            # print('недоступен')
            # print(result)
            return result

        successful_icmp_request = 0
        total_delay = 0
        for result in info:
            # print(result)
        # for result in i:
        #     print(result)
            if isinstance(result, float):
                successful_icmp_request += 1
                # print(f'{successful_icmp_request=}')
                total_delay += result
        # print(f'{successful_icmp_request=}')
        average_delay = total_delay / successful_icmp_request
        if successful_icmp_request == 3:
            execution_code = 0
            result = execution_code, host_name, host_ip, \
                round(average_delay, 3)
            if queue:
                queue.put(result)
            # print('All OK')
            return result
        else:
            execution_code = 1
            result = execution_code, host_name, host_ip,\
                round(average_delay, 3), (3 - successful_icmp_request)
            if queue:
                queue.put(result)
            # print("OK with error")
            return result
    except OSError:
        print('Проверьте работает ли у Вас сетевая карта')
        execution_code = -1
        result = execution_code, host_name, host_ip
        if queue:
            queue.put(result)
        return result


if __name__ == "__main__":
    hosts = [('google.com', 'google.com'),
             ('onliner.by', 'onliner.by'),
             ('127.0.0.1', 'my_comp'),
             ('172.19.5.110', 'NKU'),
             ('172.19.5.112', 'NKU-2'),
             ]
    data = [
        [0.05846047401428223, 0.08408832550048828, 0.061429738998413086],
        [0.09540486335754395, 0.08738088607788086, 0.08862137794494629],
        [0.05481839179992676, 0.05638599395751953, 0.05617809295654297],
        [0.0003616809844970703, 0.00034046173095703125, 0.0003154277801513672],
        [None, 0.48400211334228516, 0.061843156814575195],
    ]
    for host in hosts:
        print(handle_info_about_host(host_ip=host[0], host_name=host[1]))
    # handle_info_about_host('ss', 'aa')
