# Задание 1

# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования,
# реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере),
# класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.

import time


class Device():
    def __init__(self,model, color, weight, drive, cost):
        self.model = model
        self.color = color
        self.weight = weight
        self.drive = drive
        self.cost = cost

    def __str__(self):
        return f"\
            Model device: {self.model} \n\
            Color device: {self.color} \n\
            Weight device: {self.weight} kg\n\
            Drive device: {self.drive} \n\
            Cost device:  {self.cost} $"

class Blender(Device):
    def __init__(self, model, color, weight, drive, cost, power):
        super().__init__(model, color, weight, drive, cost)
        self.power = power

    def __str__(self):
        return super().__str__() + f"\n\
            Power: {self.power}"
    
    def get_start_mixed(self):
        return f"Blender starts mixing"

    def set_speed(self,user_speed):
        return f"User speed - {user_speed}"

r8d5 = Blender(model="Tefal 57j8r",color="White",weight="4",drive="electric",cost="500",power='50kW')
start = input("Do you want to start work with blender? y/n: ")
if start == "y":
    print('======================')
    print('Hello, this is Blender')
    print('======================')
    print(r8d5)

    speed = input('Please choose the speed of mixing. Enter number 1-5: ')

    print(r8d5.set_speed(speed))
    print(r8d5.get_start_mixed())
    time.sleep(5)
    print( 'blender finished work')
else:
    print('buy buy')
print('')
print('Did work with blender tired you ? ')
print('')

class CoffeeMachine(Device):

    def get_coffee(self,coffee_type):
        if coffee_type == '1':
            return print('please take your capuchino')    
        elif coffee_type == '2':
            return print('please take your late')
            
    def set_coffee(self):
        user_choice = input('What type of coffee do you want?\n\
            1-capuchino\n\
            2-late\n\
            enter 1 or 2: ')
        print('Please wait a few seconds')
        time.sleep(5)
        return user_choice

coffee_combayn = CoffeeMachine(model='Greate mood', 
                               color='dark', 
                               weight='5.5', 
                               drive='electric', 
                               cost='1000'
                               )

coffee_time = input('Do you want a cup of coffee? y/n: ')
if coffee_time == 'y':
    print('============================')
    print('Hello, this is Coffeemachine')
    print('============================')
    print(coffee_combayn)
    coffee_combayn.get_coffee(coffee_combayn.set_coffee())
else:
    print('buy buy')        

class MeatGrinder(Device):
    def __init__(self, model, color, weight, drive, cost):
        super().__init__(model, color, weight, drive, cost)

    def get_start(self, speed):
        return print(f"MeatGrinder start to work on {speed} speed")

    def set_start(self):
        start_speed = input("choise speed for meatgrinder (1 or 2): ")
        if start_speed == "1":
            return 'low'
        else:
            return 'hight'

meat_grinder = MeatGrinder(model='52rd4v', color='grey', weight='2', drive='mechanic', cost='25')
print('This is meatgrinder')
print('====================')
print(meat_grinder)
meat_grinder.get_start(meat_grinder.set_start())
time.sleep(4)
print('meatgrinder finish work')
        