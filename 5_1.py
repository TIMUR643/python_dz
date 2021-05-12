my_list = []
while True:
    line = input("Ваш текст: ")
    if line == '':
        print(my_list)
        'exit()'
        break
    else:
        my_list.append(line)

    with open("text.txt", "w") as file:
        file.writelines(my_list)
