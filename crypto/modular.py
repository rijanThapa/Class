def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod  # Taking modulus of base with mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod

    return result

try:
    base = int(input("Enter the base number: "))
    exp = int(input("Enter the exponent: "))
    mod = int(input("Enter the modulus: "))

    if base < 0 or exp < 0 or mod <= 0:
        raise ValueError("Base and exponent must be non-negative, and modulus must be positive.")

    result = modular_exponentiation(base, exp, mod)
    print(f"{base}^{exp} mod {mod} = {result}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error: {e}")
