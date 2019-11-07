"""
code to make a list of unicode points by (list comprehension method).

"""
s='mumbai'
l=[ord(s[j])for j in range(len(s))]
print(l)
