class Robot():
    __counter = 0
    def __init__(self, name, model, year, engine):
        Robot.__counter += 1
        print('robot create', Robot.__counter)
        self.name = name
        self.model = model
        self.year = year
        self.engine = engine

    def __str__(self):
        return f"Hello, I am robot - {self.name} {self.model} {self.engine}"

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_engine(self):
        return self.engine


r2d2 = Robot(name='Amigo', model='r2d2',year=7, engine='sun_energy')
C3PO = Robot(name='Circle', model='c3po',year=5, engine='electric_energy')
print(r2d2.get_year())

