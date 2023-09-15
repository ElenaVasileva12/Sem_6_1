# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from Home_work_6 import date_true
import sys

# num,mount,year=list(map(int,input('Введите дату в формате DD.MM.YYYY: ').split('.')))
# print(date_true(num,mount,year))

options = list(map(int, sys.argv[1:]))

num_g = 11
mount_g = 12
year_g = 2014

if len(options):
    if len(options) == 3:
        num_g, mount_g, year_g = options
    else:
        print("Некорректный ввод")

print(date_true(num_g, mount_g, year_g))
