# Задание №2
#       ✔ Напишите функцию, которая принимает строку текста.
#       ✔ Сформируйте список с уникальными кодами Unicode каждого
#       символа введённой строки отсортированный по убыванию.


# def my_symbols(text: str):
#     print(list(text))

def my_symbols(text: str):
    lst =[]
    for i in set(text):
        lst.append(ord(i))
    return sorted(lst, reverse=True)


text = input('Insert text: ')
# print(*my_symbols(text), sep=', ')


# another mode of writing this function:
def my_func(text: str) -> list:
    return sorted(list(map(ord, set(text))), reverse=True)


print(*my_func(text))

