# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными 
# вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана 
# загадка или ноль, если попытки исчерпаны.
 
__dict_result = {}

def my_secret(secret, variants, attempts):
    for i in range (attempts):
        print('secret: ', secret)
        answer = input('Insert your answer: ')
        if answer in variants:
            print('Correct')
            print(f'Secret "{secret}" has been guessed with {i + 1} attempts')
            return i + 1
        else:
            print(f'It is wrong, you have {attempts - i - 1} attempts more')
    print('You have no more attempts')
    return 0 


if __name__ == '__main__':

    secret = input('Insert the secret: ')
    variants = input('Insert 3 answers using comma: ').split(',')
    attempts = int(input('Insert the number of attempts: '))


    result = my_secret(secret, variants, attempts)
    print(f'The result is: {result}')


# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки. 


def my_secret_dict():
    dict_secret = {
        'data type': ['tuple', 'list', 'str'],
        'what is blue': ['sea', 'sky', 'flower'],
        'continents': ['Asia', 'Europe', 'Australia']
    }
    for key, value in dict_secret.items():
        __dict_result[key] = my_secret(key, value, 3)
    
    return 0


# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) 
# и число (номер попытки, с которой она угадана). 
# Функция формирует словарь с информацией о результатах отгадывания. 
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря 
# в удобном для чтения виде. 
# Для формирования результатов используйте генераторное выражение.

def output_dict_result():
    for key, value in __dict_result.items():
        print(f'The secret: {key}. Has been guessed using {value} attempts ')