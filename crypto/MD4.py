from Crypto.Hash import MD4

def md4_hash(text):

    text_bytes = text.encode('utf-8')

    hash_object = MD4.new()
    

    hash_object.update(text_bytes)
    

    md4_hash = hash_object.hexdigest()
    
    return md4_hash


text = input("Enter a string to hash using MD4: ")
hashed_value = md4_hash(text)

print(f"The MD4 hash of '{text}' is: {hashed_value}")
