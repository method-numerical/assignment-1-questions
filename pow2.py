"""
eliminating found and if statement.
using while else instead.
"""
L=[1,2,4,8,16,32,64]
X=5
i=0
while not(2**X==L[i]):
    i=i+1
else:
    print('found at',i,'.')
