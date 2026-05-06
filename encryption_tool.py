print("Encryption Tool")

message = input("Please enter your Message to Encrypt: ").lower()

encryption = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}

sign_encryption = {
    'a': ",", 'b': "<", 'c': ".", 'd': ">", 'e': "/",
    'f': "?", 'g': ";", 'h': ":", 'i': "!", 'j': "-",
    'k': "(", 'l': "@", 'm': "#", 'n': "*", 'o': "!",
    'p': "^", 'q': "&", 'r': "%", 's': "%", 't': "$",
    'u': "[", 'v': "]", 'w': "?", 'x': "^", 'y': "*",
    'z': ":"
}

encrypted = []

for char in message:
    if char == " ":
        encrypted.append(" ")
    elif char in encryption:
        encrypted.append(str(encryption[char]))
    else:
        encrypted.append(char)  # keep punctuation/numbers

print("Encrypted Message:")
print(" ".join(encrypted))

print("\nNow Sign Encrypted Message:")
message_to_sign = input("Please enter your Message to Sign: ").lower()

sign_encrypted = []

for chars in message_to_sign:
    sign_encrypted.append(str(sign_encryption.get(chars, chars)))

print("Encrypted:", " ".join(sign_encrypted))
