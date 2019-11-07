"""
generalisation to add any number of keywords.

"""
def adder(**keywords):
    sum=0
    for key, value in keywords.items():
        sum=sum+value
    return sum

print(adder(a=1,b=2,c=5,d=8))
