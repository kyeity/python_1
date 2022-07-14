#lists
'''Lists

Парні індекси
Функція приймає список чисел. Потрібно вивести всі числа з парними індексами'''




'''Парні елементи
Функція приймає список чисел. Потрібно вивести всі парні елементи списку'''

def pair_elements(*nums):
    for num in nums:
        if num % 2 == 0:
            print(num, end=" ")

'''Найбільше число
Функція приймає список чисел. Потрібно вивести найбільше число і його індекс'''
def max_num(*nu):
    return max(nu), 1+nu.index(max(nu))


'''Зворотній порядок
Функція приймає список чисел. Має повернути список але у зворотному порядку'''

def reverse(*nums):
    return nums[::-1]


'''Унікальні елементи
Функція приймає список чисел. Потрібно повернути лише ті елементи що зустрічаються один раз'''

def unique(*numbers):
    from collections import Counter
    d = Counter(numbers)
    new_list = list([item for item in d if d[item] < 2])
    return (new_list)


