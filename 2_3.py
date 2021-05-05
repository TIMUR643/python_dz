number = int(input("Введите номер месяца: "))
month_dict = {1: 'Зима',
                  2: 'Зиме',
                  3: 'Весне',
                  4: 'Весне',
                  5: 'Весне',
                  6: 'Лету',
                  7: 'Лету',
                  8: 'Лету',
                  9: 'Осени',
                  10: 'Осени',
                  11: 'Осени',
                  12: 'Зиме'}
month_list = list(month_dict.values())
for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Этот месяц относиться к {month_list[i]}")
