# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию

from .task_1_2 import _leap_year

count_day={
    '01':31,
    '03':31,
    '04':30,
    '05':31,
    '06':30,
    '07':31,
    '08':31,
    '09':30,
    '10':31,
    '11':30,
    '12':31,
    }


def date_true(num,mount,year_):
     _leap=_leap_year(year_)
     if _leap==1:                     #добавили второй месяц в словарь (в зависимости от високосности)
         count_day['02']=29
     elif _leap==0:
         count_day['02']=28
    
     for k,v in count_day.items():
          if year_>=1 and year_<=9999:
               if mount == int(k):
                    if num in range(1,v+1):
                         return(f'Истина')
     else:
          return(f'Ложь')

#num,mount,year_=list(map(int,input('Введите дату в формате DD.MM.YYYY: ').split('.')))



#print(date_true(num,mount,year_))
    