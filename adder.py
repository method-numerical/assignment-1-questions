"""
adder function taking only good, bad, ugly kewwords.

"""
def adder(good,bad,ugly):
    z=good+bad+ugly
    return z
good=1; bad=2; ugly=3;    #default values....

a=adder(good=5,ugly=1)

#after executing above code error came as TypeError: adder() missing 1 required positional argument: 'bad'.

#It implies that this function must take all key words good,bad,ugly.
