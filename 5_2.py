my_list = ['text\n', 'текст\n', 'ТЕКСТ\n']
with open("textt.txt", 'w+') as file:
    file.writelines(my_list)
with open("textt.txt") as file:
    lines = 0
    letters = 0
    for line in file:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"Букв в строке {letters} ")
    print(f"Строк {lines}")
