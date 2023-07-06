# Задание №3
#       Погружение в Python | Коллекции
#        ✔ Создайте вручную кортеж содержащий элементы разных типов.
#        ✔ Получите из него словарь списков, где:
#        ключ — тип элемента,
#        значение — список элементов данного типа.

my_tuple = (1, 13, 'cat', True, 5.157, 'str', 'fff')
my_dict = {}
for i in my_tuple:
    i_t = type(i)
    if i_t not in my_dict:
        my_dict[i_t] = []
    my_dict[i_t].append(i)
print(my_dict)