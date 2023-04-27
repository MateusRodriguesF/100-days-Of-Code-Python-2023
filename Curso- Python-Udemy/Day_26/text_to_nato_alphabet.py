import pandas as pd

data = pd.read_csv(r"Day_26\nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [nato_alphabet_dict[letter] for letter in word]

print(output_list)