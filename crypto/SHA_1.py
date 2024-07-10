import hashlib

def encrypt_this_string(input_string):
    try:
    
        sha1 = hashlib.sha1()


        sha1.update(input_string.encode())


        hash_text = sha1.hexdigest()

        return hash_text

    except Exception as e:
        raise RuntimeError(e)


if __name__ == "__main__":
    print("Enter a string to calculate its SHA-1 hash:")
    user_input = input().strip()

    if user_input:
        hash_result = encrypt_this_string(user_input)
        print(f"\nSHA-1 hash for '{user_input}' is: {hash_result}")
    else:
        print("No input provided. Exiting...")
