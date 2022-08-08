

class Driver:
    name = str(None)
    expirience = str(None)

    def __init__(self, name='John Deere', expirience='1 yr,'):
        self.name = name
        self.expirience = expirience

    def __str__(self):
        return f'{self.name}, {self.expirience}'

class Engine:
    power = None
    producer = None

    def __init__(self, power='200 hp', producer='Bayerische Motoren Werke AG'):
        self.power = power
        self.producer = producer

    def __str__(self):
        return f'{self.power}, {self.producer}'

class Car(Driver, Engine):
    brand = None
    class_of_auto = None
    weight = None

    def __init__(self, brand='BMW', class_of_auto='Business', weight=2000):
        self.brand = brand
        self.class_of_auto = class_of_auto
        self.weight = weight
        #super().__init__('Tesla', brand)

    def start(self):
        return f'Поїхали,'
    def stop(self):
        return f'Зупиняємось,'
    def turnRight(self):
        return f'Поворот праворуч,'
    def turnLeft(self):
        return f'Поворот ліворуч,'

    def __str__(self):
        return f'{self.brand}, {self.class_of_auto},'

class Lorry(Car):
    def __init__(self, weight=3500):
        self.weight = weight

    def __str__(self):
        if self.weight >= 3500:
            return f'Вантажівка,'
        else:
            return f'Легковик,'

class Sportcar(Car):
    def __init__(self, max_speed=250):
        self.max_speed = max_speed

    def __str__(self):
        if self.max_speed >= 250:
            return f'Спорткар'
        else:
            return f'Слоукар'

a = Car()
b = a.turnLeft()
d = Driver()
e = Engine()
f = Lorry(350)
g = Sportcar(100)
print(d, e, a, b, f, g)

