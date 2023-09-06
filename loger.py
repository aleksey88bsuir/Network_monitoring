import logging
import traceback


app_loger = logging.getLogger('Network monitoring')

app_loger.setLevel(logging.INFO)

# настройка обработчика и форматировщика для app_loger
handler_for_func = logging.FileHandler(f"app.log", mode='a')
formatter_for_func = logging.Formatter(
    fmt='[%(asctime)s] [%(levelname)s] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S'
)

# добавление форматировщика к обработчику
handler_for_func.setFormatter(formatter_for_func)
# добавление обработчика к логгеру
app_loger.addHandler(handler_for_func)


def log_exceptions(logger=app_loger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Ошибка в функции {func.__name__}: {e}")
                logger.error(f"Входные данные: {args}, {kwargs}")
                raise
        return wrapper
    return decorator


@log_exceptions(logger=app_loger)
def my_function(x, y):
    return x / y


class LoggerWrapper:
    def __init__(self):
        self.logger = logging.getLogger('Network monitoring')
        self.setup_handlers()

    def setup_handlers(self):
        if len(self.logger.handlers) > 0:
            return
        info_handler = logging.FileHandler('app.log', mode='a')
        # error_handler = logging.FileHandler('error.log', mode='a')
        formatter_ = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s] => %(message)s',
            datefmt='%d.%m.%Y %H:%M:%S')
        info_handler.setFormatter(formatter_)
        # error_handler.setFormatter(formatter_)
        info_handler.setLevel(logging.INFO)
        # error_handler.setLevel(logging.ERROR)
        self.logger.addHandler(info_handler)
        # self.logger.addHandler(error_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message, *args, **kwargs):
        tb = traceback.format_exc()
        attributes = ", ".join([str(arg) for arg in args])
        dict_attributes = ", ".join([(str(key)+'='+str(value))
                                     for key, value in kwargs.items()])[:-1]
        log_message = (f"{message}\n{tb}Атрибуты: {attributes},"
                       f" {dict_attributes}")
        self.logger.error(log_message)


class MyClass:
    def __init__(self):
        self.logger = LoggerWrapper()
        self.a = 5
        self.b = 0
        self.c = 'some_text'
        self.logger.log_info('Произошла инициализация объекта')

    def my_method(self, a_param, b, comment=''):
        try:
            return str(a_param / b) + comment
        except Exception as e:
            self.logger.log_error(e, a_param, b, comment)


if __name__ == "__main__":
    # result = my_function(10, 0)
    a = MyClass()
    a.my_method(5, 2)
    a.my_method(a.a, a.b,  comment='ccc')
