import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        yn=input(f"Did ypu mean {get_close_matches(word,data.keys())[0]} instead? Enter Y is YES, or N if NO. ")
        if yn.upper()=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn.upper()=="N":
            return "Word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "Word doesn't exist. Please double check it."

word=input("Enter word: ")

output = translate(word.lower())

if type(output)==list:
    for item in output:
        print(item)
elif type(output)==str:
    print(output)
