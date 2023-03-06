import string
alphabet = list(string.ascii_lowercase * 2)

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}\n")

def decrypt(plainc_text, shift_amount):
    cipher_text = ""
    for letter in plainc_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}\n")
