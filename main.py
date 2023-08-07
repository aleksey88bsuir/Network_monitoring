import subprocess


def run_gui_application():
    try:
        subprocess.run(['python', 'ui/gui.py'])
    except FileNotFoundError:
        print('Error: GUI.py file not found')


run_gui_application()
