
import random



x = 25
y = 30

rand = random.randint(3, x + y - 3)

def XOrY(x,y):
    slice = random.randint(3, x + y - 9)
    if slice <= x-3:
        split = (0, slice)
    else:
        split = (1, slice - x + 3)
    return split

split = XOrY(10, 15)
    
print(split)



