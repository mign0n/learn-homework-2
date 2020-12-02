"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime as dt
from datetime import timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = dt.today()
    yesterday = today - timedelta(days=1)
    a_month_ago = today - timedelta(days=30)

    today = today.strftime('%d.%m.%Y')
    yesterday = yesterday.strftime('%d.%m.%Y')
    a_month_ago = a_month_ago.strftime('%d.%m.%Y')

    print(f"Yesterday: {yesterday},"
          f"\nToday: {today},"
          f"\n30 days ago: {a_month_ago}")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return dt.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
