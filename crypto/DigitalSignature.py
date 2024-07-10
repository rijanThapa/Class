def euclid(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return euclid(n, r)

def exteuclid(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t
        
    if t1 < 0:
        t1 = t1 % a
        
    return (r1, t1)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

p = int(input("Enter a prime number p: "))
while not is_prime(p):
    p = int(input("Invalid input. Enter a prime number p: "))

q = int(input("Enter a prime number q (different from p): "))
while not is_prime(q) or q == p:
    if q == p:
        q = int(input("q should be different from p. Enter a prime number q: "))
    else:
        q = int(input("Invalid input. Enter a prime number q: "))

n = p * q
Pn = (p-1) * (q-1)

key = []
for i in range(2, Pn):
    gcd = euclid(Pn, i)
    if gcd == 1:
        key.append(i)

e = int(input(f"Select an encryption key from {key}: "))
while e not in key:
    e = int(input(f"Invalid input. Select an encryption key from {key}: "))

r, d = exteuclid(Pn, e)
if r == 1:
    d = d % Pn

M = int(input("Enter the message (integer): "))

S = pow(M, d, n)
M1 = pow(S, e, n)

if M == M1:
    print("Accept the message sent by Alice")
else:
    print("Do not accept the message sent by Alice")
