class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"Hello my name is {self.name} I am {self.age} year"

    def say(self, sound):
        print(f"{sound} {sound}")

tuzik = Animal(name='tuzik', age='1', weight='5,5')
print(tuzik)
tuzik.say("Gav")

class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def __str__(self):
        return super().__str__()

    def chuh(self, dosmth):
        print(f"{self.name} {dosmth}")

cat_one = Cat(name='Murzik', age='5', weight='4')
print(cat_one)
cat_one.say('Myaaauu')
cat_one.chuh('cheshet lapoy uho')

class Poni(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def __str__(self):
        return super().__str__()


horse = Poni(name='KoputomVlob', age='10', weight='250')
print(horse)
horse.say('IgoGo')