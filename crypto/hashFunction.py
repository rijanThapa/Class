def my_hash_function(value):
    return hash(value)


user_input = input("Enter a value to hash: ")


hashed_value = my_hash_function(user_input)


print(f"The hash of '{user_input}' is: {hashed_value}")
