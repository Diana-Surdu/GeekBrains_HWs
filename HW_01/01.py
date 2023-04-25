
# Задача 2: Найдите сумму цифр трехзначного числа.

a = input('Insert a three-digit number: ')

if len(a) == 3:
    print(int(a[0]) + int(a[1]) + int(a[2]))
else:
    print('Error - this is not a three-digit number!')