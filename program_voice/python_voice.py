# import pyttsx3
# from playsound import playsound


def say_computer(name_host: str):
    engine = pyttsx3.init()
    engine.setProperty("voice", "ru")
    engine.setProperty('rate', 90)
    engine.say('Внимание')
    engine.say('Узел связи ' + name_host + ' недоступен')
    engine.runAndWait()
    engine.stop()


def say_computer_about_cable():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", "ru")
    engine.setProperty('rate', 90)
    # for voice in voices:
    #     print(voice.name)
    #     if voice.name == 'Aleksandr':
    #         engine.setProperty('voice', voice.id)
    #
    # engine.say('Командный голос вырабатываю, товарищ генерал-полковник!')

    engine.say('Внимание')
    engine.say('НЕИСПРАВНОСТЬ')
    engine.runAndWait()
    engine.stop()
