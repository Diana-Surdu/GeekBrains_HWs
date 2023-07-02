#   Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#   Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

frac_str_01 = input('Insert a fractional number: ')
frac_str_02 = input('Insert a fractional number: ')

# extract the numbers from string:
list_str_01 = frac_str_01.split('/')
list_str_02 = frac_str_02.split('/')

for i in range(0, len(list_str_01)):
    list_str_01[i] = int(list_str_01[i])

for i in range(0, len(list_str_02)):
    list_str_02[i] = int(list_str_02[i])


# calculate the sum of fractional number: 
fraction_numerator_1 = list_str_01[0] * list_str_02[1] + list_str_02[0] * list_str_01[1]
fraction_denominator_1 = list_str_01[1] * list_str_02[1]
 
print(f'{frac_str_01} + {frac_str_02} = {fraction_numerator_1}/{fraction_denominator_1}' )


# calculate multiplication of fractional number:
fraction_numerator_2 = list_str_01[0] * list_str_02[0]
fraction_denominator_2 = list_str_01[1] * list_str_02[1]

print(f'{frac_str_01} * {frac_str_02} = {fraction_numerator_2}/{fraction_denominator_2}')


print('-------------------')


# verification using franstions module
a = Fraction(frac_str_01)
b = Fraction(frac_str_02)
print(f'{frac_str_01} + {frac_str_02} = {a + b}')
print(f'{frac_str_01} * {frac_str_02} = {a * b}')








