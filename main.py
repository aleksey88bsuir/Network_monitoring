from loger import app_loger, log_exceptions
import os
import sys
from ui.gui import main


@log_exceptions(logger=app_loger)
def run_gui_application():
    try:
        sys.path.insert(0,
                     os.path.dirname(
                         os.path.dirname(os.path.realpath(__file__))))
        main()
    except FileNotFoundError:
        print('Error: GUI.py file not found')


if __name__ == "__main__":
    run_gui_application()
