alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def ceasar_decryption(encrypted_text, shift):
    decrypted_text = ""
    n = len(encrypted_text)
    for i in range(n):
        c = encrypted_text[i]
        loc = alpha.find(c)
        newloc = (loc - shift) % 26
        decrypted_text += alpha[newloc]
    return decrypted_text

def caesar_brute_force(ciphertext):
    for shift in range(26):
        decrypted_text = ceasar_decryption(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

ciphertext = 'ZRUOG'
caesar_brute_force(ciphertext)
