# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

a = int(input('Insert a number that represents the first side of the triangle: '))
b = int(input('Insert a number that represents the second side of the triangle: '))
c = int(input('Insert a number that represents the third side of the triangle: '))


if (a+b)>c and (a+c)>b and (b+c)>a:
    if (a!=b and b!=c and a!=c):
        result = "This is a scalene triangle"
    elif (a==b and a!=c) or (a==c and c!=b) or (c==b and c!=a):
        result = "This is a isosceles triangle"
    elif a==b==c:
        result = "This is a eqculateral triangle"
else:
    result = "It's not a triangle"

print(result)
