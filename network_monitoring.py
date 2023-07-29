from ping3 import ping


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
        result.append(ping(host_ip))
    return tuple(result)


def handle_info_about_host(host_ip: str, host_name: str,
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
        if any(info) is None:
            execution_code = -1
            result = execution_code, host_ip, host_name
            if queue:
                queue.put(result)
            return result
        if all(info) is False:
            execution_code = 2
            result = execution_code, host_ip, host_name
            if queue:
                queue.put(result)
            return result
        successful_icmp_request = 0
        total_delay = 0
        for result in info:
            if isinstance(result, float):
                successful_icmp_request += 1
                total_delay += result
        average_delay = total_delay / successful_icmp_request
        if successful_icmp_request == 3:
            execution_code = 0
            result = execution_code, host_ip, host_name, \
                round(average_delay, 3)
            if queue:
                queue.put(result)
            return result
        else:
            execution_code = 1
            result = execution_code, host_ip, host_name,\
                round(average_delay, 3), (3 - successful_icmp_request)
            if queue:
                queue.put(result)
            return result
    except OSError:
        print('Проверьте работает ли у Вас сетевая карта')
        execution_code = -1
        result = execution_code, host_ip, host_name
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
    for host in hosts:
        print(handle_info_about_host(host_ip=host[0], host_name=host[1]))
