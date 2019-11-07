"""
to calculate first 100 fiboacci numbers & time needed.

"""
import fibonacci
import timeit
a=fibonacci.fibonacci(100)

code="""
import fibonacci
a=fibonacci.fibonacci(100)
"""
t=timeit.timeit(code,number=1)
print('time needed = ',t,'seconds.')
