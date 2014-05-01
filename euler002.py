total = 0
a = 1
b = 1
while (b <= 4 * 10**6):
    a, b = b, a+b
    if (b%2 == 0):
        total += b
print total
