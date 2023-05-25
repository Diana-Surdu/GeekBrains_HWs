# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
#             В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
#             D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
#             А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
#             Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
#             Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается 
#             только одно слово, которое содержит либо только английские, либо только русские буквы.


# price = {'A, E, I, O, U, L, N, S, T, R': 1, 'D, G': 2, 'B, C, M, P': 3, 'F, H, V, W, Y': 4, 'K': 5, 'J, X': 8,  'Q, Z': 10, 'А, В, Е, И, Н, О, Р, С, Т': 1,  'Д, К, Л, М, П, У': 2, 'Б, Г, Ё, Ь, Я': 3,  'Й, Ы': 4, 'Ж, З, Х, Ц, Ч': 5,  'Ш, Э, Ю': 8, 'Ф, Щ, Ъ': 10}

# word = input('Insert a word: ').upper()
# s = 0
# for i in range(len(price)):
#     for letter in word:
#         if letter in list(price.keys())[1]:
#             s += list(price.values()[i])
# print('You get {s} points')

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5:'K', 8: 'JX',  10: 'QZ'}
# point_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',  4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = input().upper
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in point_en[j]:
#                 count = count + j
#     else:
#         for j in points_ru:
#             if i in point_ru[j]:
#                 count = count + j
# print(count)

price = {'A, E, I, O, U, L, N, S, T, R': 1, 'D, G': 2, 'B, C, M, P': 3, 'F, H, V, W, Y': 4, 'K': 5, 'J, X': 8,  'Q, Z': 10, 'А, В, Е, И, Н, О, Р, С, Т': 1,  'Д, К, Л, М, П, У': 2, 'Б, Г, Ё, Ь, Я': 3,  'Й, Ы': 4, 'Ж, З, Х, Ц, Ч': 5,  'Ш, Э, Ю': 8, 'Ф, Щ, Ъ': 10}

word = input('Insert a word: ').upper()
s = 0
for i in range(len(price)):
    for letter in word:
        if letter in list(price.keys())[i]:
            s += list(price.values())[i]
print(f'You get {s} points!!!')