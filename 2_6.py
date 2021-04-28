
inventory_tuple_list = []
i = 1
while True:
    inventory_tuple_list.append(
        (input('Введите номер товара: '), dict({
            'название товаров': str(input('Введите название: ')),
            'цены': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
            'eд': str(input('Введите единцы измерения: ')),
        }))
    )

    if input('Товар добавлен. Добавить еще один товар? (y/n): ') == 'n':
        break

    i += 1

print(f'список товаров:{inventory_tuple_list}')

output_dict = dict({})
for product in inventory_tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(output_dict)
