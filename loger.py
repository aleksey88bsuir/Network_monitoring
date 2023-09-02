import logging


app_loger = logging.getLogger('Network monitoring')

app_loger.setLevel(logging.INFO)

# настройка обработчика и форматировщика для app_loger
handler = logging.FileHandler(f"app.log", mode='a')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
handler.setFormatter(formatter)
# добавление обработчика к логгеру
app_loger.addHandler(handler)


def log_exceptions(logger):
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


if __name__ == "__main__":
    result = my_function(10, 0)

