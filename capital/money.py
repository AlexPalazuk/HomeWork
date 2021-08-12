from os import closerange
from cheks import check_number 

with open("./capital/file.txt", mode="r") as file:
    bank = file.read()
    print('your bank is: ', bank)
bank = int(bank)



home_bank = [bank]

def put_money():
    money = input('Enter how match money put: ')
    
    while check_number(money) == False:
        print('Wrong, you must enter integer!!!!!')
        money = input('Enter how match money put: ')
        check_number(money)

    money = int(money)
    return home_bank.append(money)

def ask():
    asked = input('do you want put more money? y/n: ')
    while asked=='y':
        put_money()
        asked = input('do you want put more money? y/n: ')

put_money()
ask()

a = 0
for i in home_bank:
    a += i
  
del home_bank[0:]
home_bank.append(a)
print(home_bank)
for i in home_bank:
    money = i 

def get_money(money):
    costs = int(input('Enter your cost: '))
    new_money = money - costs
    return str(new_money)
new_bank = get_money(money)
print('Your new capital is: ', new_bank)
with open("./capital/file.txt", mode="w") as file:
    file.write(new_bank)
