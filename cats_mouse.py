def catAndMouse(x, y, z):
    a = abs(z - x)
    b = abs(z - y)
    
    if a > b:
        return "Cat B"
    if a < b:
        return "Cat A"
    else:
        return "Mouse C"