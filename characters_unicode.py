"""
code to print sum of  unicodes of characters of a string.

"""
s='mumbai'
for j in range(1,len(s)):
    f=ord(s[j])+ord(s[j-1])
    j=j+1
print('sum of unicode is :=',f)
