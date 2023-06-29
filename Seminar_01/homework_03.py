#  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
#  должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
#  числа используйте код:
#       from random import randint
#       num = randint(LOWER_LIMIT, UPPER_LIMIT) 


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRIES = 10
count = 1

import random
num = random.randint(LOWER_LIMIT,UPPER_LIMIT)
print (num)

print('Insert a number between', LOWER_LIMIT, 'and',UPPER_LIMIT, '? ')
your_number = int(input())

while count < TRIES:
    if your_number > LOWER_LIMIT and your_number < UPPER_LIMIT:
        if num > your_number:
            print('Try a bigger number')
            your_number = int(input())
        elif num < your_number:
            print('Try a smaller number') 
            your_number = int(input())  
        elif your_number < LOWER_LIMIT or your_number > UPPER_LIMIT:
            print('Wrong')
        elif num == your_number:
            print('Congratulations! You have guessed the number using', count, 'tries')
            break
    else:
        print("You insert a wrong number! Please, try again!")
        break
    count += 1
else:
    print('Unfortunately you have used all chances!')
    quit()

