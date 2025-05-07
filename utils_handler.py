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
