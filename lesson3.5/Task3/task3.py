# Дан текстовый файл.
# Удалить из него последнюю строку. 
# Результат записать в другой файл.
with open("./Task3/file3-1.txt", mode='r') as file:
    last_line = file.readlines()
with open("./Task3/file3-2.txt", mode='w') as file2:
    for i in last_line[:-1]:
        file2.write(f"{i}")