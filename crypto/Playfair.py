def create_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # The letter ’J’ is omitted

    # Initialize the Playfair matrix with zeros
    matrix = [['' for _ in range(5)] for _ in range(5)]

    # Fill the matrix with the key
    used_letters = set()
    row, col = 0, 0

    for letter in key:
        if letter not in used_letters:
            matrix[row][col] = letter
            used_letters.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1

    # Fill the remaining empty cells with the alphabet
    for letter in alphabet:
        if letter not in used_letters:
            matrix[row][col] = letter
            used_letters.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix

def prepare_text(text):
    text = text.replace(" ", "").upper()

    text = text.replace("J", "I")
    
   
    if len(text) % 2 != 0:
        text += 'X'
    
  
    digrams = []
    i = 0
    while i < len(text):
        if i + 1 < len(text): 
            if text[i] == text[i + 1]:
                digrams.append(text[i] + 'X')
            else:
                digrams.append(text[i] + text[i + 1])
            i += 2
        else:  
            digrams.append(text[i] + 'X')
            i += 1
    
    return digrams

    text = text.replace(" ", "").upper()
  
    text = text.replace("J", "I")
    
    
    if len(text) % 2 != 0:
        text += 'X'
    

    digrams = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            digrams.append(text[i] + 'X')
            i += 1
        else:
            digrams.append(text[i] + text[i + 1])
            i += 2
    return digrams

def encrypt_playfair(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = []

    for digram in plaintext:
        row1, col1 = None, None
        row2, col2 = None, None

        for row in range(5):
            for col in range(5):
                if matrix[row][col] == digram[0]:
                    row1, col1 = row, col
                if matrix[row][col] == digram[1]:
                    row2, col2 = row, col

        
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        ciphertext.append(matrix[row1][col1] + matrix[row2][col2])

    return ''.join(ciphertext)

def decrypt_playfair(ciphertext, key):
    matrix = create_playfair_matrix(key)
    ciphertext = prepare_text(ciphertext)
    plaintext = []

    for digram in ciphertext:
        row1, col1 = None, None
        row2, col2 = None, None

      
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == digram[0]:
                    row1, col1 = row, col
                if matrix[row][col] == digram[1]:
                    row2, col2 = row, col

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        plaintext.append(matrix[row1][col1] + matrix[row2][col2])

    return ''.join(plaintext)


key = "KEYWORD"
plaintext = "HELLO WORLD"
ciphertext = encrypt_playfair(plaintext, key)
decrypted_text = decrypt_playfair(ciphertext, key)

print("Original Text:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
