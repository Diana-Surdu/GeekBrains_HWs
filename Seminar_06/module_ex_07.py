# Создайте модуль и напишите в нём функцию, которая получает 
# на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или 
# ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне 
# [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь. Проверку года на 
# високосность вынести в отдельную защищённую функцию.


def my_data(user_data):
    day, month, year = map(int, user_data.split('.'))

    if day not in range (1, 32) or month not in range (1, 13) or year not in range(1, 10000):
        return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
        return True
    elif month in [4, 6, 9, 11] and day in range(1,31):
        return True
    elif month == 2:
        if _leep_year(year) is True and day > 28:
            return False
        elif _leep_year(year) is False and day > 29:
            return True
    else:
        return False
    

def _leep_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return True
    else:
        return False
    
def print_data():
    user_data = input('Insert date that has DD.MM.YYYY format: ')
    result = my_data(user_data)
    if result is True:
        print('This date exists')
    else:
        print("This date doesn't exist")

    
if __name__ == '__main___':
    
    print_data()