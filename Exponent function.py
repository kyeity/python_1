# возведение в степени (первая цифра, вторая степень)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
# вывод
print(raise_to_power(2, 4))