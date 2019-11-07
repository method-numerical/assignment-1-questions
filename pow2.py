"""
improving the previous code.
moving 2**X expression out of the loop....
"""
L=[]
X=5
for i in range(6):
    L.append(2**i)
a=L.index(2**X)     #now out of loop

if a>-1:
    print('found at',a,'.')
else:
    print('not found....')
