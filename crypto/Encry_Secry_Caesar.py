alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def contains_only_alphabets(input_str):
    for char in input_str:
        if not char.isalpha():
            return False
    return True

while True:
    try:
        msg = input("Input message: ")
        if contains_only_alphabets(msg):
            break
        else:
            print("Input message does not contain alphabets only!")
    except ValueError:
        print("Input is not alphabetic. Try again!")

while True:
    try:
        key = int(input("Enter a number between 1 and 26: "))
        if 1 <= key <= 26:
            break
        else:
            print("Input is not between 1 and 26. Try again.")
    except ValueError:
        print("Input is not an integer. Try again.")

def ceasar_encryption(text, shift):
    encrypted_text = ""
    text = text.upper()
    n = len(text)
    for i in range(n):
        c = text[i]
        loc = alpha.find(c)
        newloc = (loc + shift) % 26
        encrypted_text += alpha[newloc]
    return encrypted_text

def ceasar_decryption(encrypted_text, shift):
    decrypted_text = ""
    n = len(encrypted_text)
    for i in range(n):
        c = encrypted_text[i]
        loc = alpha.find(c)
        newloc = (loc - shift) % 26
        decrypted_text += alpha[newloc]
    return decrypted_text

ciphertext = ceasar_encryption(msg, key)
decrypted_text = ceasar_decryption(ciphertext, key)
print("Plaintext:", msg)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
