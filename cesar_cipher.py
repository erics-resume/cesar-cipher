# Generate code
# password = "I_LiKE_hiBachi"

# encrypt text
def encrypt(password, s):
    # scramble text
    result = ""

    # traverse text
    for i in range(len(password)):
        char = password[i]

        # Encrypt uppercase letters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase letters
        else:
            result += chr((ord(char) + s- 97) % 26 + 97)
    return result


# decrypt text
def decrypt(encrypted_text, s):
    # unscramble cesar cipher code
    plaintext = ""
    # traverse cipher text
    for char in encrypted_text:
    # decrypt letter
        if char.isalpha():
            char_code = ord(char)
            # when char is lowercase
            if char.islower():
                char_code -= s
                if char_code < ord('a'):
                    char_code += 26
            else:
                char_code -= s
                if char_code < ord('A'):
                    char_code += 26
            plaintext += chr(char_code)
    # if character is not alphabetic
    else:
        plaintext += char
    return plaintext


if __name__ == '__main__':
    get_letter, keyword = 0, []

    # Enter password and key
    text = str(input("Enter the text: "))
    key = int(input("Enter the key: "))
    cipher_text = encrypt(text,key)
    decrypted_text = decrypt(cipher_text, key)

    print("Text : " + text)
    print("Shift : " + str(key))
    print("Cipher: " + cipher_text)

    print("Now I want the text decrypted")
    print("Decrypted Text: " + decrypted_text)
