import os
from db.work_with_table_hosts import WorkWithUnionTables
import subprocess
from loger import app_loger, log_exceptions


wwut = WorkWithUnionTables()


@log_exceptions(logger=app_loger)
def get_music_file(folder):
    # folder = os.path.abspath(folder)
    music_files = list()
    music_files.append('')
    for root, dirs, files in os.walk(folder):
        for filename in files:
            music_files.append(filename.split('/')[-1])
    return music_files


@log_exceptions(logger=app_loger)
def open_file(file_path):
    try:
        subprocess.run(['open', file_path])
    except FileNotFoundError:
        print('Error: No default text editor found')


@log_exceptions(logger=app_loger)
def show_host_status_history(id_host):
    info = wwut.read_info_about_status(id_host)
    write_info_about_status(info)


@log_exceptions(logger=app_loger)
def show_host_status_history_with_time(id_host, st_time, fin_time):
    info = wwut.read_info_about_status_with_time(id_host, st_time, fin_time)
    write_info_about_status(info)


@log_exceptions(logger=app_loger)
def show_host_lp_history(id_host):
    info = wwut.read_info_about_lp(id_host)
    write_info_about_lp(info)


@log_exceptions(logger=app_loger)
def show_host_lp_history_with_time(id_host, st_time, fin_time):
    info = wwut.read_info_about_lp_with_time(id_host, st_time, fin_time)
    write_info_about_lp(info)


@log_exceptions(logger=app_loger)
def write_info_about_status(info):
    with (open('report.txt', 'w') as file):
        if info:
            demarcation_line = '-'*85 + '\n'
            first_line = (f'|{"№ п/п":^5}|'
                          f'{"Имя хоста":^20}|'
                          f'{"ip адрес хоста":^20}|'
                          f'{"статус в сети":^14}|'
                          f'{"время события":^20}|\n')
            file.write(demarcation_line)
            file.write(first_line)
            file.write(demarcation_line)
            for i, row in enumerate(info):
                string = (f'|{i+1:^5}|'
                          f'{row[0]:^20}|'
                          f'{row[1]:^20}|'
                          f'{row[2]:^14}|'
                          f'{row[3].strftime("%d.%m.%Y %H:%M:%S"):^20}|\n')
                file.write(string)
                file.write(demarcation_line)
        else:
            file.write('База данных пуста')
    open_file('report.txt')


@log_exceptions(logger=app_loger)
def write_info_about_lp(info):
    with (open('report.txt', 'w') as file):
        if info:
            demarcation_line = '-'*96 + '\n'
            first_line = (f'|{"№ п/п":^5}|'
                          f'{"Имя хоста":^20}|'
                          f'{"ip адрес хоста":^20}|'
                          f'{"кол-во потерянных пакетов":^25}|'
                          f'{"время события":^20}|\n')
            file.write(demarcation_line)
            file.write(first_line)
            file.write(demarcation_line)
            for i, row in enumerate(info):
                string = (f'|{i+1:^5}|'
                          f'{row[0]:^20}|'
                          f'{row[1]:^20}|'
                          f'{row[2]:^25}|'
                          f'{row[3].strftime("%d.%m.%Y %H:%M:%S"):^20}|\n')
                file.write(string)
                file.write(demarcation_line)
        else:
            file.write('База данных пуста')
    open_file('report.txt')


if __name__ == "__main__":
    print(get_music_file('../program_voice/voice_files/'))
