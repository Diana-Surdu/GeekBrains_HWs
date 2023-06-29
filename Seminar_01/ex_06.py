# Задание №6
#       Напишите программу, которая запрашивает год и проверяет его на високосность.
#       Распишите все возможные проверки в цепочке elif
#       Откажитесь от магических чисел
#       Обязательно учтите год ввода Григорианского календаря
#       В коде должны быть один input и один print

LEAP_YEAR_4 = 4
LEAP_YEAR_400 = 400
LEAP_YEAR_100 = 100
GRIGORIAN_CALENDER = 1582

year = int(input('Insert year in yyyy format: '))

if year <= GRIGORIAN_CALENDER:
    s = 'This is not Grigorian Calender'
elif (year % LEAP_YEAR_4 == 0 or year % LEAP_YEAR_400 == 0) and year % LEAP_YEAR_100 != 0:
    s ='A leap year'
else:
    s = 'Not a leap year'
print(s)