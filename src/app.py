import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# loading the json data as python dict
data = json.load(open("data.json"))


# Function for retrieving a definition
def retrieve_definition(word):
    # check if the word exists in the dict
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist yet.")
        else:
            return ("We don't understand your entry, sorry.")

    else:
        return ("The word doesn't exist in the database, please double check.")


# Input from user

word_user = input("Enter a word: ")

# Retrieve the def using the function and print the result

output = retrieve_definition(word_user)

# If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-", item)
#  For words having single definition
else:
    print("-", output)

