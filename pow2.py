"""
eliminating found and if statement.
using if else instead.
"""
L=[1,2,4,8,16,32,64]
X=5
i=0
for i in range(6):
    if L[i]==2**X:
        print('found at',i,'.')
    else:
        i=i+1
