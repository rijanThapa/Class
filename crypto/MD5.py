import hashlib

def md5_hash(text):

    text_bytes = text.encode('utf-8')
    
    
    hash_object = hashlib.md5()
    
    hash_object.update(text_bytes)
    
   
    md5_hash = hash_object.hexdigest()
    
    return md5_hash


text = input("Enter a string to hash using MD5: ")
hashed_value = md5_hash(text)

print(f"The MD5 hash of '{text}' is: {hashed_value}")
