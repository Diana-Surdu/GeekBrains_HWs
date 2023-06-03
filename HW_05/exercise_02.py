# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
#              и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
#         A = 3; B = 5 -> 243 (3⁵)
#         A = 2; B = 3 -> 8 

base = int(input('Insert the number that represents the base of the exponentiation: '))
exponent = int(input('Insert a number that represents the exponent: '))

def exponentiation(a, b):
    if b == 0:
        return 1
    return a * exponentiation(a, b-1)


print(exponentiation(base, exponent))