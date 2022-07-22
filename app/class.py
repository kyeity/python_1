
class Phone:

    '''number = str('099112432')
    model = str('Nokia')
    weight = int(200)
    name = str('Johny')'''

    def __init__(self, number, model, weight, name):
        self.number = number
        self.model = model
        self.weight = weight
        self.name = name

    def __str__(self):
        return f'{self.number}, {self.model}, {self.weight}'

    def getNumber(self):
        return self.number

    def receiveCall(self, name: str, number: str = None):
        if number is None:
            return f'Телефонує {name}'
        else:
            return f'Телефонує {name} {number}'

    def sendMessage(self, *asd):
        num_back = ' '.join(asd)
        return num_back

ph = Phone('0981231231', 'Nokia_3310', '112 kg', 'Johny')


'''print('_____________')
print(ph.receiveCall('Ivan'))
print(ph.receiveCall('0981231231'))
print(ph.receiveCall('Ivan', '0981231231'))
print(ph.__str__())
print(ph.sendMessage('0981233322', '0509998877', '0673322112'))
print('_____________')'''


class Student:

    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark
        self.age = 18


    def getScholarship(self, averageMark):
        self.averageMark = averageMark
        if averageMark >= 5:
            return f'100 грн'
        else:
            return f'80 грн'


class Aspirant(Student):

    def __init__(self, firstName, lastName, group, averageMark):
        super().__init__(firstName, lastName, group, averageMark)

    def getScholarship(self, averageMark):
        super().getScholarship(averageMark)
        self.averageMark = averageMark
        if averageMark >= 5:
            return f'200 грн'
        else:
            return f'180 грн'


student_mark = Student('Ivan', 'Korablov', '2', None)
aspirant_mark = Aspirant('Dima', 'Ivanov', '1', None)


'''print(student_mark.getScholarship(2), student_mark.lastName)
print(aspirant_mark.getScholarship(5), aspirant_mark.lastName)
print('----------------------------------------')'''

class Driver:
    #name = None
    #expirience = None

    def __init__(self, name='John Deere', expirience='1 yr'):
        self.name = name
        self.expirience = expirience

    def __str__(self):
        return f'{self.name}, {self.expirience}'

class Engine:
    #power = None
    #producer = None

    def __init__(self, power='200 hp', producer='Bayerische Motoren Werke AG'):
        self.power = power
        self.producer = producer

    def __str__(self):
        return f'{self.power}, {self.producer}'

class Car(Driver, Engine):
    '''brand = None
    class_of_auto = None
    weight = None'''

    def __init__(self, brand='BMW', class_of_auto='Business', weight=2000):
        self.brand = brand
        self.class_of_auto = class_of_auto
        self.weight = weight
        #super().__init__('Tesla', brand)

    def start(self):
        return f'Поїхали'
    def stop(self):
        return f'Зупиняємось'
    def turnRight(self):
        return f'Поворот праворуч'
    def turnLeft(self):
        return f'Поворот ліворуч'

    def __str__(self):
        return f'{self.brand}, {self.class_of_auto},'

class Lorry(Car):
    def __init__(self, weight=3500):
        self.weight = weight

    def __str__(self):
        if self.weight >= 3500:
            return f'Вантажівка'
        else:
            return f'Легковик'

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
g = Sportcar(300)
print(d, e, a, b, f, g)



'''class Cat:

    def __init__(self, name, breed='haski', age=3, color='ruby'):
        print('Hello', name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
Cat('Tom', 'siam', 40, 'black')
Cat('Jora')

class Person:
    name = 'Ivan'
    age = 30

Person.name = 'Misha'
print(Person.name)
setattr(Person, 'x', 200)
print(Person.x)
del Person.x

class Ccar:
    model = 'BMW'
    eengine = 3.6

    def drive():
        print("Let's go!")

Ccar.drive()
getattr(Ccar, 'drive')()
a = Ccar
a.drive()'''


'''class Employee():
    def __init__(self, empno, ename, salary, deptno):
        self.Empno = empno
        self.Ename = ename
        self.Salary = salary
        self.Deptno = deptno

    def showEmployee(self):
        print("Employee # : {}\nEmployee Name : {}\nSalary : {}\nDepartment : {}".format(self.Empno, self.Ename,
                                                                                         self.Salary, self.Deptno))


class Salesman(Employee):
    def __init__(self, empno, ename, salary, deptno, comm):
        self.Commission = comm
        super().__init__(empno, ename, salary, deptno)

    def showEmployee(self):
        print("Salesman Profile")
        super().showEmployee()
        print("Commision : ", self.Commission)


class CEO(Employee):
    def __init__(self, empno, ename, salary, deptno, stock):
        self.Stock = stock
        super().__init__(empno, ename, salary, deptno)

    def showEmployee(self):
        print("CEO Profile")
        super().showEmployee()
        print("Stock Options : ", self.Stock)


salesman = Salesman(200, "John Doe", 67000, "Sales", 100)
salesman.showEmployee()
print("")
ceo = CEO(40, "Jennifer Smith", 300000, "Director", 1000000)
ceo.showEmployee()'''