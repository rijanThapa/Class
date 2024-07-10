alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ "
print("Length of alpha: {}".format(len(alpha)))

str_in = input("Enter a word, like HELLO: ").upper()
shift = int(input("Input Shift value, like 3: "))

n = len(str_in)
msg_cipher = ""

for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    if loc != -1:
        newloc = (loc + shift) % 26
        msg_cipher += alpha[newloc]
    else:
        msg_cipher += c

print("Plain text:", str_in)
print("Shift Value:", shift)
print("Cipher text:", msg_cipher)

