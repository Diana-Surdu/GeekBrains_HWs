# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#            Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
#           2 2
#               4 

a = int(input('Insert the first number: '))
b = int(input('Insert the second number: '))

def sum(a, b,):
    if a == 0:
        return b
    elif b == 0:
        return a
    return sum(a-1, b+1)

print(sum(a, b))