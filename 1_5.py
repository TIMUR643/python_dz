profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
profitability = profit / costs
if profit > costs:
    print("Фирма работает с прибылью. Рентабельность выручки составила" )
    print(profitability)
    workers = int(input("Введите количество сотрудников фирмы "))
    profit1 = profit / workers
    print("прибыль в расчете на одного сторудника сотавила")
    print(profit1)
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
