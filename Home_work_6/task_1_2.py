
#проверка на високосность
def _leap_year(year: int):
    answer = "Обычный" 
    if year >= 1:
        if year % 4 == 0:
            if year % 100 != 0:
                answer = "Високосный"
            elif year % 400 == 0:
                answer = "Високосный"
    return (1 if answer=="Високосный" else 0)


# n = int(input("Введите год (4 цифры): "))
# print(leap_year(n))


# "Обычный" - 0
# "Високосный" - 1