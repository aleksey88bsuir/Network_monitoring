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
#
# logger2.info(f"Testing the custom logger for module {__name__}...")
#
# logging.basicConfig(filename='app.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


