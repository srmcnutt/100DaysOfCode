# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass



import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
# for (index, row) in data.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(row.code)

# nato_dict = {}
# for index, row in data.iterrows():
#     nato_dict[row.letter] = row.code


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}


def phonetic():
    choice = input("enter a word, and I'll return a NATO code for you: ").upper()
    try:
        word_list = [nato_dict[letter] for letter in choice]
    except KeyError:
        print("sorry.  only letters in the alphabet please")
        phonetic()
    else:
        phrase = ""
        for word in word_list:
            phrase += f"{word} "

        print(f"NATO phrase: {phrase}")

phonetic()
