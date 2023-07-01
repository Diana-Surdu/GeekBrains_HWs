# Задание №5
#       ✔ Напишите программу, которая решает
#         квадратные уравнения даже если
#         дискриминант отрицательный.
#       ✔ Используйте комплексные числа
#         для извлечения квадратного корня.


a = float(input('Insert a: '))
b = float(input('Insert b: '))
c = float(input('Insert c: '))

d = b ** 2 - 4 * a * c

if d > 0:
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    result = f'{x_1 = }, {x_2 = }'
elif d == 0:
    x = -b / (2 * a)
    result = f'{x = }'
else:
    d = complex(d, 0)
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    result = result = f'{x_1 = }, {x_2 = }'
print(result)


