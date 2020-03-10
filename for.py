vowels = 0
consonants = 0

for letter in "nehabora":
   if letter.lower() in "aeiou":
      vowels = vowels + 1
    elif letter ==" ": 
      pass

    else:
    consonants = consonants + 1


print("There are{}vowels".format(vowels))
print("there are{}consonants".format(consonants))



