def xor_encrypt(text, key):
    result = []
    for letter in text:
        result.append(chr(ord(letter) ^ key))
    return "".join(result)

def xor_decrypt(text, key):
    result = []
    for letter in text:
        result.append(chr(ord(letter) ^ key))
    return "".join(result)

def decrypt(text, key):
    result = []
    for letter in text:
        if letter.islower():
            result.append(chr((ord(letter) - ord('a') - key) % 26 + ord('a')))
        elif letter.isupper():
            result.append(chr((ord(letter) - ord('A') - key) % 26 + ord('A')))
        else:
            result.append(letter)  # spaces and symbols stay the same

    return "".join(result)


def encrypt(text, key):
    result = []
    for letter in text:
        if letter.islower():
            result.append(chr((ord(letter) - ord('a') + key) % 26 + ord('a')))
        elif letter.isupper():
            result.append(chr((ord(letter) - ord('A') + key) % 26 + ord('A')))
        else:
            result.append(letter)  # spaces and symbols stay the same

    return "".join(result)

def vignere_encrypt(text, key):
    result = []
    for i, letter in enumerate(text):
        if letter.islower():
            result.append(chr((ord(letter) - ord('a') + ord(key[i % len(key)]) - ord('a')) % 26 + ord('a')))
        elif letter.isupper():
            result.append(chr((ord(letter) - ord('A') + ord(key[i % len(key)]) - ord('a')) % 26 + ord('A')))
        else:
            result.append(letter)

    return "".join(result)
def vignere_decrypt(text, key):
    result = []
    for i, letter in enumerate(text):
        if letter.islower():
            result.append(chr(((ord(letter) - ord('a') - (ord(key[i % len(key)]) - ord('a'))) % 26 + ord('a'))))
        elif letter.isupper():
            result.append(chr(((ord(letter) - ord('A') - (ord(key[i % len(key)]) - ord('a'))) % 26 + ord('A'))))
        else:
            result.append(letter)
    return "".join(result)

print("choose cipher")
print("1. Caesar")
print("2. Vigenere")
print("3. XOR")
cipher = int(input("cipher: "))

print("Choose operation:")
print("1. Encrypt")
print("2. Decrypt")
operation = int(input("operation:"))

if cipher == 1:
    text = input("enter text:")
    key = int(input("enter key:"))
    if operation == 1:
        print(f" Encrypted version is", encrypt(text, key))
    elif operation == 2:
        print(f" Decrypted version is", decrypt(text, key))
    else:
        print("Invalid operation")
elif cipher == 2:
    text = input("enter text:")
    key = input("enter key:")
    
    if operation == 1:
        print(f" Encrypted version is", vignere_encrypt(text, key))
    elif operation == 2:
        print(f" Decrypted version is", vignere_decrypt(text, key))
    else:
        print("Invalid operation")
elif cipher == 3:
    text = input("enter text:")
    key = int(input("enter key:"))
    if operation == 1:
        print(f" Encrypted version is", xor_encrypt(text, key))
    elif operation == 2:
        print(f" Decrypted version is", xor_decrypt(text, key))
    else:
        print("Invalid operation")
else:
    print("Invalid operation")
