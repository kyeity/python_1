
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


print('_____________')
print(ph.receiveCall('Ivan'))
print(ph.receiveCall('0981231231'))
print(ph.receiveCall('Ivan', '0981231231'))
print(ph.__str__())
print(ph.sendMessage('0981233322', '0509998877', '0673322112'))
print('_____________')