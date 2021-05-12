
from itertools import count
from math import factorial
def factorial_gen():
    for el in count(1):
        yield factorial(el)
gen = factorial_gen()
x = 0
for i in gen:
    if x < 3:
        print(i)
        x += 1

    else:
       break
