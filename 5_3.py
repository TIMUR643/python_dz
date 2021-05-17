company = {'Иванов': 30000, 'Петров': 100000, 'Сидоров': 90000, }
try:
    file = open("texxt.txt", 'w')
    for last_name, salary in company.items():
        file.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file.close()
summ = 0
count = 0
persons = []
with open("texxt.txt", "r") as file:
    for line in file:
        print(line, end="")
        a = line.split(':')
        if int(a[1]) <= 200:
            persons.append(a[0])
        summ += int(a[1])
        count += 1
result = summ / count
print(f"Средний доход: {result}")
