#     Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#               если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Insert the number of squares that the chocolate bar has vertically: '))
m = int(input('Insert the number of squares that the chocolate has horizontally: '))
k = int(input('Insert the number of squares that has been broken off from the chocolate bar: '))

if k < n * m:
    if k % n == 0 or k % m == 0:
        print('You can break off the chocolate bar!')
    else:
        print("You can't break off the chocolate bar!")
else:
    print('Error! Check the insert data, something is wrong!!!')