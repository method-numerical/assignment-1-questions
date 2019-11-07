"""
single line code to generate first 10 fibonacci numbers.

"""
from functools import reduce
a=lambda n: reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0,1])
print(a(10))
