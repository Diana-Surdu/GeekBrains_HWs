# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 10,'hello', 3, 2, 1, 3.14, 7, 5, 3.14, 7, 10, 'hello']
new_list = []
for i in my_list:
    if my_list.count(i) == 2:
        new_list += [i]
my_list = list(set(new_list))
print(my_list)