# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
#             разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#             Каждое число вводится с новой строки.

a1 = int(input('Insert a number: '))
d = int(input('Insert a number: '))
n = int(input('Insert a number: '))

for i in range(n):
    print(a1 + i * d)