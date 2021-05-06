
def script():
time=float(input('Введите время работы в часах : '))
salary=float(input('Введите зарплату в час : '))
bonus=float(input('Введите премию - '))
pay=time*salary+bonus
return pay
print(f'Размер зарплаты составил: {script()}')
 
  
  
  
  
  
in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [num1 for num1, num2 in zip(in_list[1☺, in_list[:-1]) if num1 > num2]
print(res_list)
 
                                       
                                       
                                       
for i in range(20, 240,20):
print(i)
for a in range(20,240,21):
print(a)

                                       
                                       
my_list = [1, 2, 2, 3, 4, 1, 2]
new = [el for el in my_list if my_list.count(el)==1]
print(new)
 
    
                                       
                                       
from functools import reduce
def my_func(el_p, el):
return el_p * el
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')
 
                                       
                                       
                                       
                                       
                                       
from itertools import count
from itertools import cycle

def count_func(start_number, stop_number):
for el in count(start_number):
if el > stop_number:
break
else:
print(el)
def cycle_func(my_list, iteration):
i = 0
iter = cycle(my_list)
while i < iteration:
print(next(iter))
i+=1
count_func(start_number = int(input("enter start number: ")), stop_number = int(input("enter stop number: ")))
cycle_func(my_list = [1, 2], iteration = int(input("enter iteration: ")))
 
                                       
                                       
                                       
                                       
from itertools import count
from math import factorial
def fibo_gen():
    for el in count(1):
        yield factorial(el)
gen = fibo_gen()
x = 0
for i in gen:
    if x < 3:
        print(i)
        x += 1
    else:
        break
