import datetime


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


def get_datetime_now():
    return datetime.datetime.now().strftime("%d%m%Y")


def get_first_day_of_month():
    return datetime.datetime.now().replace(day=1).strftime("%d%m%Y")
