"""
generalisation to add any number of keywords.

"""
def adder(**num):
    sum=0
    for key, value in num.items():
        sum=sum+value
    return sum

print(adder(a=1,b=2,c=5,d=8))
