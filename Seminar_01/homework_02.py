#  Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Insert a number: '))

ONE = 1
LIMIT = 100000

if (num > ONE  and num <= LIMIT):
    if ( num % ONE == 0 and num % num == 0 and num % 2 != 0):
        print(num, "- is a simple number")
    else:
        print(num, "- is a compound number")
else:
    print("Something is wrong!!! Your number should be a positive one and not bigger than", LIMIT)

