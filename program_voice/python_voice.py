import pyttsx3
from playsound import playsound
from loger import app_loger, log_exceptions


class PyVoice:
    volume_level = 0.7

    @classmethod
    @log_exceptions(logger=app_loger)
    def say_computer(cls, name_host: str):
        engine = pyttsx3.init()
        engine.setProperty("voice", "ru")
        engine.setProperty('rate', 90)
        engine.setProperty('volume', cls.volume_level)
        engine.say('Внимание')
        engine.say('Узел связи ' + name_host + ' недоступен')
        engine.runAndWait()
        engine.stop()

    @classmethod
    @log_exceptions(logger=app_loger)
    def say_computer_about_cable(cls):
        engine = pyttsx3.init()
        # voices = engine.getProperty('voices')
        engine.setProperty("voice", "ru")
        engine.setProperty('rate', 90)
        engine.setProperty('volume', cls.volume_level)
        # engine.setProperty('volume', volume_level)
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


if __name__ == "__main__":
    playsound('voice_files/boom.wav')
