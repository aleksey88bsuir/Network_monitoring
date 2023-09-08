import subprocess
from loger import app_loger, log_exceptions
import os


@log_exceptions(logger=app_loger)
def run_gui_application():
    try:
        parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        parent_dir += '/network_monitoring_attempt_2'
        env = os.environ.copy()
        env["PYTHONPATH"] = parent_dir
        subprocess.run(["python", "ui/gui.py"], env=env)
    except FileNotFoundError:
        print('Error: GUI.py file not found')


if __name__ == "__main__":
    run_gui_application()
