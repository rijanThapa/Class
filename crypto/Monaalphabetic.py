import random


alphabet = "abcdefghijklmnopqrstuvwxyz"


random.seed(42) 
cipher_alphabet = list(alphabet)
random.shuffle(cipher_alphabet)
cipher_alphabet = ''.join(cipher_alphabet)

print("Alphabet: ", alphabet)
print("Shuffled alphabet:", cipher_alphabet)

encryption_mapping = {}
decryption_mapping = {}

for i in range(len(alphabet)):
    encryption_mapping[alphabet[i]] = cipher_alphabet[i]
    decryption_mapping[cipher_alphabet[i]] = alphabet[i]

print("Encryption mapping:\n", encryption_mapping)
print("Decryption mapping:\n", decryption_mapping)


def encrypt(message):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
        
            if char.isupper():
                encrypted_message += encryption_mapping[char.lower()].upper()
            else:
                encrypted_message += encryption_mapping[char]
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(ciphertext):
    decrypted_message = ""

    for char in ciphertext:
        if char.isalpha():
           
            if char.isupper():
                decrypted_message += decryption_mapping[char.lower()].upper()
            else:
                decrypted_message += decryption_mapping[char]
        else:
            decrypted_message += char

    return decrypted_message


message = input("Input message to encrypt: ")


cipher_text = encrypt(message)


decrypted_message = decrypt(cipher_text)

print("Plaintext: ", message)
print("Cipher text: ", cipher_text)
print("Decrypted text: ", decrypted_message)
