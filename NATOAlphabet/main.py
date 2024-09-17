import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter:row.code for (index, row) in data.iterrows()} 

def get_input():
    try:
        user_name = input("Enter Your Text: ").upper()
        code_user = [code_dict[char] for char in user_name]
        print(code_user)
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
        get_input()

get_input()

