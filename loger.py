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
