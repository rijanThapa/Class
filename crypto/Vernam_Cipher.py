import random

def generate_random_key(message_length):
    return [random.randint(0, 1) for _ in range(message_length)]

def encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Key length must match the plaintext length")
    
    ciphertext = [str(int(plaintext[i]) ^ key[i]) for i in range(len(plaintext))]
    
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Key length must match the ciphertext length")
    
    plaintext = [str(int(ciphertext[i]) ^ key[i]) for i in range(len(ciphertext))]
    
    return ''.join(plaintext)


message = "Hello World!"
message_bits = [int(bit) for bit in ''.join(format(ord(char), '08b') for char in message)]
key = generate_random_key(len(message_bits))

key_stream = ''.join(str(bit) for bit in key)

ciphertext = encrypt(message_bits, key)
decrypted_message_bits = decrypt(ciphertext, key)

decrypted_message = ''.join(chr(int(decrypted_message_bits[i:i+8], 2)) for i in range(0, len(decrypted_message_bits), 8))

print("Original Message:", message)
print("Length of message:", len(message))
print("Key:", key_stream)
print("Cipher text (in bits):", ''.join(map(str, ciphertext)))
print("Length of key:", len(key))
print("Length of encrypted message:", len(ciphertext))
print("Decrypted text:", decrypted_message)
