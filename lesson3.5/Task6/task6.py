# Дан текстовый файл. Найти и заменить в нем заданное слово.
# Что искать и на что заменять определяется пользователем.
with open("./Task6/file6.txt", mode = "r") as file:
    file_text = file.read()

file_text = file_text.replace("world", "wonderfull world")

with open("./Task6/file6.txt", mode = "w") as file1:
    file1.write(file_text)