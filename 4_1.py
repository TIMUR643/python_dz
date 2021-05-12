def script():
    time=float(input('Введите время работы в часах : '))
    salary=float(input('Введите зарплату в час : '))
    bonus=float(input('Введите премию - '))
    pay=time*salary+bonus
    return pay
print(f'Размер зарплаты составил: {script()}')