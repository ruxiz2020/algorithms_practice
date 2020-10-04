def fastPower(a, b, n):
    if n == 1:
        return a % b
    elif n == 0:
        # do not use `1` instead `1 % b` because `b = 1`
        return 1 % b
    elif n < 0:
        return -1

    # (a * b) % p = ((a % p) * (b % p)) % p
    product = fastPower(a, b, n // 2)
    product = (product * product) % b
    if n % 2 == 1:
        product = (product * a) % b

    return product


a = 4
b = 2
n = 5

print('a, b, n')
print(a, b, n)
print(fastPower(a, b, n))

print(a**n % b)
