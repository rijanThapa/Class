def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    encrypted_text = []
    key_length = len(keyword)

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(keyword[i % key_length]) - ord('A')
            encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(plaintext[i])

    return ''.join(encrypted_text)

def vigenere_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    decrypted_text = []
    key_length = len(keyword)

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(keyword[i % key_length]) - ord('A')
            decrypted_char = chr(((ord(ciphertext[i]) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(ciphertext[i])

    return ''.join(decrypted_text)


plaintext = input("Input a message: ")
keyword = "KEY"  
encrypted_text = vigenere_encrypt(plaintext, keyword)
decrypted_text = vigenere_decrypt(encrypted_text, keyword)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
