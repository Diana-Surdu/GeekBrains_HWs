#    Напишите программу, которая получает целое число и возвращает 
#    его шестнадцатеричное строковое представление. 
#    Функцию hex используйте для проверки своего результата.



number = int(input('Insert a number: '))

HEX = 16

def function_hex(number: int, mode: int) -> str:
    result = ''
    while number:
        result = str(number % mode) + result
        number //= mode
    return '0x' + result

print(hex(number), '==', function_hex(number, HEX))