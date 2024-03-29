#cicles

'''Cycle
Парні числа
Функція приймає 2 числа, має вивести всі парні числа між ними'''

def even_numbers(a, b):
    list = range(a, b) or range(b, a)
    num = []
    for x in list:
        if x % 2 == 0:
            num.append(x)
    return num


'''Дільники числа
Функція приймає єдине число, має вивести всі дільники цього числа'''

def division(a):
    for x in range(1, a+1):
        if a % x == 0:
            print(x)

'''Кількість дільників числа
Функція приймає єдине число, має вивести кількість дільників цього числа'''

def count_divisors(a):
  x = len([i for i in range(1, a+1) if not a % i])
  return x


'''Сумма чисел
Функція приймає будь яку кількість чисел, має порахувати і вивести їх сумму'''

def summaring(*args):
    return sum(args)


'''Нуль
Функція приймає будь яку кількість чисел, має вивести “Yes” якщо серед них є нуль і “No” якщо немає'''

def zero_show(*args):
    if args.__contains__(0):
        return "Yes"
    else:
        return "No"
