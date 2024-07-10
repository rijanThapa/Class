alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Length of alpha:", len(alpha))

str_in = input("Enter a word in uppercase, like HELLO: ")
print("str_in =", str_in)

msg_cipher = ""

n = len(str_in)
print("n =", n)

for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    if loc != -1:
        newloc = (loc + 3) % 26
        msg_cipher += alpha[newloc]
    else:
        msg_cipher += c

print("Plain text:", str_in)
print("Cipher text:", msg_cipher)
