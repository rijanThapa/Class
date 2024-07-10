def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1  
    gcd, x1, y1 = extended_gcd(b % a, a)


    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse does not exist for {a} mod {m}")
    else:
        return x % m


a, b = 35, 15
g, x, y = extended_gcd(a, b)
print(f"gcd({a}, {b}) = {g}")
print(f"x = {x}, y = {y}")
print(f"Verification: {g} = {a}*{x} + {b}*{y}")


a = 17
m = 43
inverse = mod_inverse(a, m)
print(f"The modular inverse of {a} mod {m} is: {inverse}")
print(f"Verification: {a} * {inverse} mod {m} = {(a * inverse) % m}")
