
list = [1, -7, 'True', True, 9.9]
def my_type(el):
    for el in range(len(list)):
        print(type(list[el]))
        print((list[el]))
    return
my_type(list)
--------------------------------
my_list = ['1', '2', '3', '4', '5']
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)

-----------------------------

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
  -------------------------------------------------------------------      
        my_str = input("ведите строку: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{el}")
    
    ---------------------------
    
number = int(input("Введите номер: "))
my_list = [1, 2, 3, 4]
a = my_list.count(number)
for element in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
------------------------------------------------
inventory_tuple_list = []
i = 1
while True:
    inventory_tuple_list.append(
        (input('Введите номер товара: '), dict({
            'название': str(input('Введите название: ')),
            'цена': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
            'eд': str(input('Введите единцы измерения: ')),
        }))
    )
