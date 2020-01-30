import random
i = 1
q = random.randint(1, 100)
while i <= q:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(1, 100)
    if (x - z) > (y - z):
        print("Cat B")
    elif (x - z) < (y - z):
        print("Cat A")
    elif (x - z) == (y - z):
        print("Mouse C")
    i += 1