
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

print(student_mark.getScholarship(2), student_mark.lastName)
print(aspirant_mark.getScholarship(5), aspirant_mark.lastName)
print('----------------------------------------')