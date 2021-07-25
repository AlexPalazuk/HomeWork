from os import closerange


with open("./Task2/file1.txt", mode="r") as file:
    full_lines = len(file.readlines())
    print('Количество строк: ',full_lines)

with open("./Task2/file1.txt", mode="r") as file:
    full_file = file.read()
    print('Количество символов: ',len(full_file))



vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
consonants_list = [ 
                    'b', 'c', 'd', 'f',\
                    'g', 'h', 'j', 'k',\
                    'l', 'm', 'n', 'p',\
                    'q', 's', 't', 'v',\
                    'w', 'x', 'z' 
                  ]
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def calculator(full_file, some_list):
    a = 0
    for i in full_file:
        if i in some_list:
            a +=1
    return a
    
vowels = calculator(full_file, vowels_list)
consonants = calculator(full_file, consonants_list)
numbers = calculator(full_file, numbers_list)
print("Количество гласных букв: ", vowels)
print("Количество согласных букв: ", consonants)
print("Количество цифр: ", numbers)

with open("./Task2/file2.txt", mode="w") as file:
    file.write(f" Количество строк: {full_lines},\
    \n Количество символов: {len(full_file)},\
    \n Количество гласных букв: {vowels},\
    \n Количество согласных букв: {consonants},\
    \n Количество цифр: {numbers}  ")       