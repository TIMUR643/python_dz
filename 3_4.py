def power(a, n):
    res = 1
    if isinstance(a, float) and a >= 0:
        #print("ok")
        if isinstance(n, int) and n <= 0:
            for i in range(abs(n)):
                res *= a

            return print(1 / res)
        else:
            return print("error")
    else:
        return print("error")

power(float(input("Первое значение - ")), int(input("Второе значение - ")))
