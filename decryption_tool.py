# ------------------------------
# DICTIONARIES
# ------------------------------

# Number encryption dictionary
number_encryption = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}

# Sign encryption dictionary (single-character symbols)
sign_encryption = {
    'a': ",", 'b': "<", 'c': ".", 'd': ">", 'e': "/",
    'f': "?", 'g': ";", 'h': ":", 'i': "!", 'j': "-",
    'k': "(", 'l': "@", 'm': "#", 'n': "*", 'o': "!",
    'p': "^", 'q': "&", 'r': "%", 's': "%", 't': "$",
    'u': "[", 'v': "]", 'w': "?", 'x': "^", 'y': "*",
    'z': ":"
}

# ------------------------------
# REVERSE DICTIONARIES FOR DECRYPTION
# ------------------------------

number_decryption = {str(v): k for k, v in number_encryption.items()}
sign_decryption = {v: k for k, v in sign_encryption.items()}

# ------------------------------
# DECRYPTION
# ------------------------------

print("DECRYPTION TOOL")
print("1. Number Decryption (a=1, b=2...)")
print("2. Sign Decryption (symbols)")

choice = input("Choose type (1 or 2): ")

if choice == "1":
    encrypted_number = input("Enter number-encrypted message: ").split()
    decrypted_number = [number_decryption.get(c, c) for c in encrypted_number]
    print("Decrypted Message:", "".join(decrypted_number))

elif choice == "2":
    encrypted_sign = input("Enter sign-encrypted message: ")
    decrypted_sign = [sign_decryption.get(c, c) for c in encrypted_sign]
    print("Decrypted Message:", "".join(decrypted_sign))

else:
    print("Invalid choice!")
