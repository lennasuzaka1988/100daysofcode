import pandas as pd

# Created dictionary in following format:
# {"A": "Alfa", "B": "Bravo"}
# with open("../nato_alphabet/nato_phonetic_alphabet.csv", "r") as nato:
#     nato_csv = pd.read_csv(nato)
#     nato_df = pd.DataFrame(nato_csv)
#     nato_dict = pd.Series(nato_df.code.values, index=nato_df.letter).to_dict()

# Created a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word: ")
# cipher_nato = [nato_dict[i.upper()] for i in word]
# print(cipher_nato)

# With error handling this time!
data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


def output_phonetic_alphabet():
    word = input("Enter a word: ").upper()
    try:
        output = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        output_phonetic_alphabet()
    else:
        print(output)


output_phonetic_alphabet()