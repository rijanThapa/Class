import random

def generate_one_time_pad(length):
    """Generate a random one-time pad of the specified length."""
    return [random.randint(0, 25) for _ in range(length)]

def otp_encrypt(text, one_time_pad):
    """Encrypt plaintext using the one-time pad."""
    if len(text) != len(one_time_pad):
        raise ValueError("Plaintext and one-time pad must be of the same length")

    encrypted_text = []
    for i in range(len(text)):
        char = text[i].upper()
        if char.isalpha():
            shift = one_time_pad[i]
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def otp_decrypt(ciphertext, one_time_pad):
    """Decrypt ciphertext using the one-time pad."""
    if len(ciphertext) != len(one_time_pad):
        raise ValueError("Ciphertext and one-time pad must be of the same length")

    decrypted_text = []
    for i in range(len(ciphertext)):
        char = ciphertext[i].upper()
        if char.isalpha():
            shift = one_time_pad[i]
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


plaintext = input("Input a message: ")
one_time_pad = generate_one_time_pad(len(plaintext))
encrypted_text = otp_encrypt(plaintext, one_time_pad)
decrypted_text = otp_decrypt(encrypted_text, one_time_pad)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
