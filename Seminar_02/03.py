# Задание №3
#       ✔ Напишите программу, которая получает целое число и возвращает
#          его двоичное, восьмеричное строковое представление.
#       ✔ Функции bin и oct используйте для проверки своего
#          результата, а не для решения.
#          Дополнительно:
#       ✔ Попробуйте избежать дублирования кода
#          в преобразованиях к разным системам счисления
#       ✔ Избегайте магических чисел
#       ✔ Добавьте аннотацию типов где это возможно

number = int(input('Insert a number: ')) 

BIN = 2
OCT = 8


def our_function(number: int, mode: int) -> str:
    result: str = ''
    while number:
        result = str(number % mode) + result
        number //= mode
    return result

print(bin(number), '==', '0b' + our_function(number, BIN))
print(oct(number), '==', '0o' + our_function(number, OCT))


if bin(number) == '0b' + our_function(number, BIN):
    print(True)

if oct(number) == '0o' + our_function(number, OCT):
    print(True)