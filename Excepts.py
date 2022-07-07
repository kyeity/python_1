
try:
# это просто дополнительно
    value = 10 / 0
# это основной код
    number = int(input("Enter a number: "))
    print(number)

# для деления на 0
except ZeroDivisionError as err:
    print(err)
# end
except ValueError:
    print("Invalid input")
