def gcd(x, y):

    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd


a = 9
b = 36
print(a, b)

print(gcd(a, b))
