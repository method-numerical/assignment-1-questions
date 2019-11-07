"""
addition of any orbitrary numbers.generalisation to add any number of keywords.

"""
def adder(*num):
    sum=0
    for j in num:
        sum=sum+j
    return sum
