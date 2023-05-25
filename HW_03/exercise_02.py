# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#             Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#             В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число 


N = int(input('Insert the number that represents the length of the list:'))

#create an empty list:
A = [] # another method is: A = list()
for i in range(N):
    A.append(int(input('Insert the elements of the list:')))
print(A)

X = int(input('Insert a number:'))
min = abs(X - A[0])
index = 0
for i in range(1, N):
    count = abs(X - A[i])
    if count < min:
        min = count
        index = i
print(f'The number {A[index]} of list A is closest in magnitude to number {X}, and their difference is {abs(X - A[index])}.')




