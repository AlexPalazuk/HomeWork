home_bank = []

def put_money():
    money = int(input('Enter how match money put: '))
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
    return print(new_money)
get_money(money)
 



