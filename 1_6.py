a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
days = 1
if a > b:
    print(days)
else:
    while a < b:
        a = a + 0.1 * a
        days += 1

    print(days)
    
