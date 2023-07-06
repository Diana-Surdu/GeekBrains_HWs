# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

my_text = 'The word culture is derived from the Latin root cultura or cultus meaning to "inhabit,\
      cultivate, or honour". In general, culture refers to human activity; different definitions of\
          culture reflect different theories for understanding, or criteria for valuing human activity. \
            Present-day anthropologists use the term to refer to the universal human capacity to classify \
                experiences and to encode and communicate them symbolically. They regard this capacity as a \
                    defining feature of the genus Homo. Since culture is learned, people living in different places \
                        have different cultures. There can be different cultures in different countries, and there can also \
                            be shared cultures among continents'

new_text = my_text.replace('"', '').replace(',', '').replace(';', '').replace('.', '').replace('-', '').lower()
new_list = new_text.split()


new_dict = {}

for i in new_list: 
    if i not in new_dict.keys():
        new_dict[i] = 1
    elif i in new_dict.keys():
        new_dict[i] += 1


most_frequently_words = []

for i in range(10):
    max_val = max(new_dict, key = new_dict.get)
    new_dict.pop(max_val)
    most_frequently_words.append(max_val)

print(f'The most frequently used words are: {most_frequently_words}')





