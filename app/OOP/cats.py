class Cat:

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
ceo.showEmployee()