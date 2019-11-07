"""
creating a fibonacci module.
"""
def fibonacci(n):
    f=[0,1]
    for j in range(2,n):
        f.append(f[j-1]+f[j-2])
        j=j+1
    for k in range(0,n):
        print('f(',k+1,')=',f[k])
        k=k+1
