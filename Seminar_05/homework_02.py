# Напишите однострочный генератор словаря, 
# который принимает на вход три списка одинаковой 
# длины: имена str, ставка int, премия str с указанием 
# процентов вида “10.25%”. В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def create_sal_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Diana", "John", "Mary"]
salaries = [35000, 20000, 10000]
bonuses = ["15.50%", "10.25%", "20.50%"]

sal_dict = create_sal_dict(names, salaries, bonuses)
print(sal_dict)

