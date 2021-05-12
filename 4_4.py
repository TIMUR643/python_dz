my_list = [1, 2, 2, 3, 4, 1, 2]
new = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(new)
