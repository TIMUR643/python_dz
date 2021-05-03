def power(a, n):
    res = 1
    if n >= 0:
        return print('ошибка')
    else:
        for i in range(abs(n)):
            res *= a

        return 1 / res


print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))
