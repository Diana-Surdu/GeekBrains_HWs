# Задание №1
#           Погружение в Python | Функции
#           ✔ Напишите функцию, которая принимает строку текста.
#           Вывести функцией каждое слово с новой строки.
#           ✔ Строки нумеруются начиная с единицы.
#           ✔ Слова выводятся отсортированными согласно кодировки Unicode.
#           ✔ Текст выравнивается по правому краю так, чтобы у самого
#           длинного слова был один пробел между ним и номером строки.

def my_func(text: str) -> None:
    text_sort = sorted(text)
    maxx = len(max(text_sort, key=len))
    for i, el in enumerate(text_sort, start=1):
        print(f'{i} {el : >{maxx}}')

text = input().split()
my_func(text)