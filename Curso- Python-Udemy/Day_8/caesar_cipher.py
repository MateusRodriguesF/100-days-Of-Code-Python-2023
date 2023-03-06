from replit import clear
from cipher import encrypt
from cipher import decrypt
from art import logo

keep = "s"
while keep == "s":

    print (logo)
    print("\n")

    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    text = input("Type your  message:\n").lower()

    shift = int(input("Type the shift number:\n"))
  
    # Logical

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(plainc_text=text, shift_amount=shift)
    
    qut = input("Want to run again?: y/n:\n")
    if qut == "y":
        keep = "s"
        print("Bye")
        clear()
    elif qut == "n":
        keep = "n"
        break
    else:
        print("Invalid input")


