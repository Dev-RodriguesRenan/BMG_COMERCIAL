import datetime
import os
import time
import shutil


def check_if_the_day_is_useful():
    if datetime.datetime.now().weekday() in [5, 6]:
        return False
    return True


def take_last_business_day():
    if check_if_the_day_is_useful():
        util_day = datetime.datetime.now() - datetime.timedelta(days=1)
    else:
        util_day = datetime.datetime.now() - datetime.timedelta(days=3)
    return util_day.strftime("%d%m%Y")


def get_name_file(action):
    curent_date = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    return f"Relatorio{action}_{curent_date}_consolidado"


def get_name_file_of_unit(action, unit):
    curent_date = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    return f"Relatorio{action}_{curent_date}_{unit}"


def get_current_date():
    return datetime.datetime.now().strftime("%Y%m%d_")


def get_datetime_now():
    return datetime.datetime.now().strftime("%d%m%Y")


def get_first_day_of_month():
    return datetime.datetime.now().replace(day=1).strftime("%d%m%Y")


def move_files_to_bkp_folder(file_path, bkp_folder):
    """Move files to a backup folder.

    Args:
        file_path (str): Path of the file to be moved.
        bkp_folder (str, optional): Path of the backup folder. Defaults to os.path.join(BASE_DOCUMENTS,'bkp').
    """
    if not os.path.exists(bkp_folder):
        os.makedirs(bkp_folder)
    try:
        shutil.move(file_path, bkp_folder)
        print(
            f"{time.strftime('%X')} >>> Arquivo {file_path} movido para a pasta de backup."
        )
    except Exception as e:
        print(
            f"{time.strftime('%X')} >>> Erro ao mover o arquivo {file_path} para a pasta de backup: {e}"
        )
