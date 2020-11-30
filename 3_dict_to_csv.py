"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
        {'name': 'John', 'age': 23, 'job': 'exorcist'},
        {'name': 'Bill', 'age': 35, 'job': 'president'},
        {'name': 'Maria', 'age': 27, 'job': 'signer'},
        {'name': 'Jack', 'age': 33, 'job': 'pirate'},
        {'name': 'Neil', 'age': 39, 'job': 'astronaut'}
    ]
    fields = 'name', 'age', 'job'
    with open('persons.csv', 'w') as file:
        writer = csv.DictWriter(file, fields, delimiter=',')
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    main()
