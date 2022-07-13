#lists
'''Lists

Парні індекси
Функція приймає список чисел. Потрібно вивести всі числа з парними індексами'''

def pair_indexes(*nums):
    for num in nums:
        if num % 2 == 0:
            print(num, end=", ")


'''Парні елементи
Функція приймає список чисел. Потрібно вивести всі парні елементи списку'''



'''Найбільше число
Функція приймає список чисел. Потрібно вивести найбільше число і його індекс'''


'''Зворотній порядок
Функція приймає список чисел. Має повернути список але у зворотному порядку'''

def reverse(*nums):
    return nums[::-1]


'''Унікальні елементи
Функція приймає список чисел. Потрібно повернути лише ті елементи що зустрічаються один раз'''
