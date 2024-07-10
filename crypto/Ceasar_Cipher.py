def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): 
            is_upper = char.isupper()  
            char = char.lower() 
            char_code = ord(char) 

           
            shifted_char_code = (char_code - 97 + shift) % 26 + 97
            encrypted_char = chr(shifted_char_code)

            if is_upper:  
                encrypted_char = encrypted_char.upper()

            encrypted_text += encrypted_char
        else:
            encrypted_text += char 

    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)

            shifted_char_code = (char_code - 97 - shift) % 26 + 97
            decrypted_char = chr(shifted_char_code)

            if is_upper:
                decrypted_char = decrypted_char.upper()

            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text



plaintext = input("Input a message: ")
shift = 3

encrypted_text = caesar_encrypt(plaintext, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
