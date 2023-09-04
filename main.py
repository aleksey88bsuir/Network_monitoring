import subprocess
from loger import app_loger,  log_exceptions


@log_exceptions(logger=app_loger)
def run_gui_application():
    try:
        subprocess.run(['python', 'ui/gui.py'])
    except FileNotFoundError:
        print('Error: GUI.py file not found')


run_gui_application()
