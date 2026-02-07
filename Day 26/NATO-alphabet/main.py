import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data_path = "Day 26/NATO-alphabet/nato_phonetic_alphabet.csv"
df = pd.read_csv(data_path)
print(df)

#TODO 1. Create a dictionary from the Data Frame:

nato_dict ={row.letter:row.code for (index,row) in df.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_name = (input("What is your name ? ")).upper()
print(user_name)

nato_user_name = [(letter,nato_dict[letter]) for letter in user_name]


print(nato_user_name)


