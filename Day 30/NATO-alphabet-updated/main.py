import pandas as pd

data_path = "Day 30/NATO-alphabet-updated/nato_phonetic_alphabet.csv"
df = pd.read_csv(data_path)

# Create a dictionary from the Data Frame:

nato_dict ={row.letter:row.code for (index,row) in df.iterrows()}
print(nato_dict)

# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetics():
    user_name = (input("What is your name ? ")).upper()
    try:
        nato_user_name = [(letter,nato_dict[letter]) for letter in user_name]
    except KeyError:
        print("Sorry, only letterss of the alphabet please.")  
        generate_phonetics() 
    else:     
        print(user_name)
        print(nato_user_name)


generate_phonetics()