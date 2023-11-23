import random
import string

class pass_gen:
    def ranGenerator():
        letters_low = list(string.ascii_lowercase)
        letters_up = list(string.ascii_uppercase)
        numbers = range(0,10)
        symbols = ["*", "@", "#", "$", "%", "&", "!", "?"]

        password_list = []
        for n in range(3):
            password_list.append(random.choice(letters_up))
            password_list.append(random.choice(letters_low))
            password_list.append(str(random.choice(numbers)))
            password_list.append(random.choice(symbols))
        random.shuffle(password_list)
        # Final Result
        rnd_psswd = ""
        for char in password_list:
            rnd_psswd += char
            
        return str(rnd_psswd)
  