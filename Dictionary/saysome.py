def sentenceMaker(phrase):
    
    capitalized = phrase.capitalize()
    interogatives = ("why","how","what")
    if phrase.startswith(interogatives):
        return f"{capitalized}?"
    else: 
        return f"{capitalized}."

results = []
while True:
    
    phrase = input("Say Something: ")           
    if phrase == "/END":
        break
    else:
        results.append(sentenceMaker( phrase.lstrip().rstrip()))

print(" ".join(results))