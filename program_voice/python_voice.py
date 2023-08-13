import pyttsx3
from playsound import playsound
from loger import app_loger


class PyVoice:
    volume_level = 0.7

    @classmethod
    def say_computer(cls, name_host: str):
        try:
            engine = pyttsx3.init()
            engine.setProperty("voice", "ru")
            engine.setProperty('rate', 90)
            engine.setProperty('volume', cls.volume_level)
            engine.say('Внимание')
            engine.say('Узел связи ' + name_host + ' недоступен')
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            app_loger.error(e)
            print('player')
            print(e)

    @classmethod
    def say_computer_about_cable(cls):
        try:
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
        except Exception as e:
            app_loger.error(e)
            print('player')
            print(e)


if __name__ == "__main__":
    playsound('voice_files/boom.wav')
