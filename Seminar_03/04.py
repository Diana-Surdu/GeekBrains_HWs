# Задание №4
#       Погружение в Python | Коллекции
#       ✔ Создайте вручную список с повторяющимися элементами.
#       ✔ Удалите из него все элементы, которые встречаются дважды

my_list = [1, 2, 3, 2, 1, 1, 5, 7,]
unic_list = []
for i in set(my_list):
    if my_list.count(i) == 1:
        unic_list += [i]
my_list = unic_list
print(my_list)


