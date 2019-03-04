import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if(word in data):
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead ? if yes, press Y if no, press N : " % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "Enter the correct word"

    else:
        return("Wrong word entered....Please check your spelling")


word=input("Enter the word : ")
print(translate(word))
