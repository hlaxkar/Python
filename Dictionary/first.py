import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
     return data[w]
    elif len(get_close_matches(w, data.keys(),cutoff=0.8)) >0:
        close = get_close_matches(w, data.keys(),cutoff=0.8)
        ans  = input("Did you mean --- %s --- instead? Y or N: " % close[0]).lower()
        if ans == "y":
            return data[close[0]]
        elif ans == "n":
                return "The word doesn't exist! Please double check it."
        else : 
            return "We didnt understand your input."        
    else:
        return "The word doesn't exist! Please double check it."

print("-----WELCOME TO DUCK DICTIONARY!--------")
word = input("Enter the word: ")
if word == "Shanya":
    print("A very lazy couch potato that sleeps all day and stays up all night.")
output = translate(word)
i = 0
if type(output) == list:
    for item in output:
        i = i+1
        print(i,".",item)
        print("---------------------")
else: print (output)        
