# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
#            решкой, а некоторые – гербом. Определите минимальное число
#            монеток, которые нужно перевернуть, чтобы все монетки были
#            повернуты вверх одной и той же стороной. Выведите минимальное
#            количество монет, которые нужно перевернуть.

n = int(input('Insert total number of coins: '))
count_n = 0
count_x = 0
count_y = 0

while count_n < n:
    N = int(input('Insert the side of the coin - "1" or "0": '))
    if N == 1 or N == 0:
        count_n += 1
        if N == 1:
            count_x += 1
        else:
            count_y += 1 
    else:
        print('Error! You can choose 1 or 0!')
if count_x < count_y:  
    print('The number of coins we have to reversed to have the same side is - ', count_x)
elif count_y < count_x:
    print('The number of coins we have to reversed to have the same side is - ', count_y)