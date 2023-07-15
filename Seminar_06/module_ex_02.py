# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: 
# нижнюю и верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных 
# границах и пользователь должен угадать его за заданное 
# число попыток. Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны 
# - ложь.
from random import randint

def find_number(a: int, b: int, nr_tries: int) -> bool:
    number = randint(a, b)
    while nr_tries:
        our_number = int(input('Insert a number: '))
        if our_number == number:
            return True
        elif our_number > number:
            print('Our number is bigger than the number we must guess')
        else:
            print('Our number is smaller than the number we must guess')
        nr_tries -= 1
    return False


if __name__ == '__find_number__':
    find_number()
