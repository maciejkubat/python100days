import pandas as p
import re

data = p.read_csv('nato_phonetic_alphabet.csv')

naval_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
cleaned_word = re.sub(r'[^a-zA-Z]', '', word)

naval_word = [naval_dict[letter] for letter in cleaned_word]

print(' '.join(naval_word))


