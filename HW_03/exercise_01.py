# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#            Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#            В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.


N = int(input('Insert the number that represents the length of the list: '))

# create a empty list:
A = []  # another solution is -  A = list()

for i in range(N):
    A.append(int(input('Insert the values of the list:')))

X = int(input('Insert the number you are looking for: '))
# create a new variable like counter:
count = 0

for i in range(len(A)):
    if A[i] == X:
        count += 1
print('The number', X, 'is repeated', count, 'times.')



