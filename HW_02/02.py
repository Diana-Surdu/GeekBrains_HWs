# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
#            школьница. Петя помогает Кате по математике. Он задумывает два
#            натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
#            этого Петя делает две подсказки. Он называет сумму этих чисел S и их
#            произведение P. Помогите Кате отгадать задуманные Петей числа.


sum = int(input('Insert the sum: '))
prod = int(input('Insert the multiplication: '))
x = 0
y = 0

#       x + y = sum           x = sum - y
#                        =>                           =>    y**2 - sum * y + prod = 0
#       x * y = prod          (sum - y) * y = prod

a = 1
b = -1 * sum
c = prod

# (a * y**2) + (b * y) + c = 0

delta = b**2 - 4*a*c

if delta > 0:
    y = (sum + delta**0.5) / 2
    x = sum - y
elif delta == 0:
    y = sum / 2
    x = sum -y

if x<=1000 and y<=1000:
    print ("The number are: ", int(x), int(y))
else:
    print("ERROR!!! The number are too big for Masha's age!!!")




