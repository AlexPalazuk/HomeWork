# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.

# Задание 2

# Реализуйте класс «Книга».
# Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

# Задание 3

# Реализуйте класс «Стадион». 
# Необходимо хранить в полях класса: 
# название стадиона, дату открытия, страну, город, вместимость. 
# Реализуйте методы класса для ввода данных, вывода данных, 
# реализуйте доступ к отдельным полям через методы класса.



class Car:
    def __init__(self, model, year, brand, engine, color, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.engine = engine
        self.color = color
        self.price = price

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_brand(self):
        return self.brand

    def get_engine(self):
        return self.engine

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_price(self,new_price):
        self.price = new_price
        return self.price

    def set_color(self, new_color):
        self.color = new_color
        return self.color

       
audi = Car(model='a8', year='2018',brand='audi', engine='2,5', color='white', price='35000')
skoda = Car(model='a7', year='2021', brand='Skoda',engine='1,8', color='green', price='25000')
print(audi.get_color())
print(audi.set_color('green'))
print(skoda.get_price())
print(skoda.set_price('15000'))


# =============================TASK 2=========================


class Book:
    def __init__(self, book_name, year, publishing_house, genre, author, price):
        self.book_name = book_name
        self.year = year
        self.publishing_house = publishing_house
        self.genre = genre
        self.author = author
        self.price = price

    def get_name(self):
        return self.book_name

    def get_year(self):
        return self.year

    def get_publishing_house(self):
        return self.publishing_house

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def set_price(self,new_price):
        self.price = new_price
        return self.price

    def set_publishing_house(self, new_publisher):
        self.publishing_house = new_publisher
        return self.publishing_house

new_book = Book('Human Physiology', '2008', 'medicine', 'educational literature','Vladimir Filimonov', '500')
print(new_book.get_name())
print(new_book.get_year())
print(new_book.get_publishing_house())
print(new_book.get_genre())
print(new_book.get_author())
print(new_book.get_price())
print(new_book.set_price('350'))


    