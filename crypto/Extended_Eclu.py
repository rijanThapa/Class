def gcd_extended(a, b):
    # Base case
    if a == 0:
        return b, 0, 1
    
    # Recursive call
    gcd, x1, y1 = gcd_extended(b % a, a)
    
    # Update x and y
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def are_relatively_prime(a, b):
    gcd, _, _ = gcd_extended(a, b)
    return gcd == 1

# Example usage:
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

gcd, x, y = gcd_extended(a, b)
print(f"gcd({a}, {b}) = {gcd}")

if are_relatively_prime(a, b):
    print(f"{a} and {b} are relatively prime.")
else:
    print(f"{a} and {b} are not relatively prime.")
