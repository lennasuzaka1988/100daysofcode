import pandas as pd

# Created dictionary in following format:
# {"A": "Alfa", "B": "Bravo"}
with open("../nato_alphabet/nato_phonetic_alphabet.csv", "r") as nato:
    nato_csv = pd.read_csv(nato)
    nato_df = pd.DataFrame(nato_csv)
    nato_dict = pd.Series(nato_df.code.values, index=nato_df.letter).to_dict()

# Created a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
cipher_nato = [nato_dict[i.upper()] for i in word]
print(cipher_nato)
