
#CONVERT LOWER CASE TO UPPER
sentence = input("Enter a sentence: ") #Senetence input

#EMPTY STRING INITIALISATION
result = ""


for char in sentence:  #FOR LOOP TO READ CHARACTERS

    if char.islower():  #LOWER CASE CHARACTER CHECK

        result += char.upper()  #LOWER CASE TO UPPER CASE
    else:

        result += char  #NO CHANGES IF THE CHARACTER IS UPPER CASE


print("Converted Sentence:", result)  #CONVERTED SENTENCE