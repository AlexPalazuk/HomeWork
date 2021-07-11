# Дан текстовый файл. Найти длину самой длинной строки.
with open("./Task4/file4.txt", mode="r") as file:
    list_str =  file.readlines()
    len_str = 0
    for i in list_str:
        if len(i) > len_str:
            len_str = len(i)
        else:
            pass
print('Длинна самой длинной строки: ',len_str, 'символа')

