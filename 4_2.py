in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [el for el in in_list if el > in_list[in_list.index(el)-1]]
print(res_list)
