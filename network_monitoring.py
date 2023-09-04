from ping3 import ping
from time import sleep
from loger import app_loger, log_exceptions


@log_exceptions(logger=app_loger)
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
    return tuple(result)


@log_exceptions(logger=app_loger)
def handle_info_about_host(host_id: str, host_ip: str,
                           queue=None) -> tuple:
    """
    Обрабатывает информацию, полученную от check_host
    :param host_ip: ip адрес хоста
    :param host_id: id хоста (узла связи)
    :param queue: Объект класса Queue. Необходим для работы в многопоточном
    режиме
    :return: возвращает результат обработки информации, полученной от хоста
    в виде кортежа
    execution_code = error: произошла непредвиденная ошибка
    execution_code = online: запрашиваемый узел доступен, пингуется без ошибок
    execution_code = online_with_error: Присутствуют ошибки при пинге
    запрашиваемого узла
    execution_code = offline: запрашиваемый узел недоступен
    """
    info = __check_host(host_ip)
    if any(elem is False for elem in info):
        execution_code = 'error'
        result = host_id, host_ip, *info, execution_code
        if queue:
            queue.put(result)
        return result

    elif all(elem is None for elem in info):
        execution_code = 'offline'
        result = host_id, *info, execution_code
        if queue:
            queue.put(result)
        return result

    elif all(isinstance(elem, float) for elem in info):
        execution_code = 'online'
        result = host_id, host_ip, *info, execution_code
        if queue:
            queue.put(result)
        return result

    else:
        execution_code = 'online_with_error'
        result = host_id, host_ip, *info, execution_code
        if queue:
            queue.put(result)
        return result
