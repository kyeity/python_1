# input numbers
num1 = int(input("Введіть першу цифру: "))
num2 = int(input("Введіть другу цифру: "))
difference1 = num1 - num2 - 1
difference2 = num2 - num1 - 1

# show numbers between num1 and num2
if difference1 >= 1:
    for x in range(difference1):
        if (x % 2 != 0):
            print(x + 3)
else:
    for x in range(difference2):
        if (x % 2 != 0):
            print(x + 3)