import pandas

alphabetData = pandas.read_csv("nato_phonetic_alphabet.csv")

phoneticDict = {row.letter: row.code for (index, row) in alphabetData.iterrows()}

word = input("Enter a word: ").upper()

for letter in word:
    print(phoneticDict[letter])