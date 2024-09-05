import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter:row.code for (index, row) in data.iterrows()} 

user_name = input("Enter Your Text: ").upper()
code_user = [code_dict[char] for char in user_name]
print(code_user)
