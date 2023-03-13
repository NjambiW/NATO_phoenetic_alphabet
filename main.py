import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("enter a word. ").upper()
    try:
        letters = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        print(f"sorry, {error_message} is not in the alphabet")
        generate_phonetic()
    else:
        print(letters)


generate_phonetic()