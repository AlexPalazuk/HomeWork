# Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.
with open("./Task5/file5.txt", mode='r') as file:
    file_text = file.read().splitlines()
words_number = 0
word = 'shine'
for i in file_text:
    new_file = i.split(' ')
    for some_word in new_file:
        if some_word == word:
            words_number += 1
print(f"В текстовом файле слово {word} встречается : {words_number} раз.")






