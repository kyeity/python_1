inputs = []
while True:
    sval = input("Enter a number: ")
    if sval == "":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    try:
        inputs.append(int(sval))
    except:
        inputs.append(float(sval))
print(sum(inputs))