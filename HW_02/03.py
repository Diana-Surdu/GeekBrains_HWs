# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Insert a number: '))
i = 0
m = 1

while m < N:
      m = 2 ** i
      i += 1
      if m <= N:
        print (m)

