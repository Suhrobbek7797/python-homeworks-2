sentence = input("Enter Text: ")

words = sentence.split()
acronym =""

for w in words:
    acronym += w[0].upper()

print(acronym)

# Answer
#Enter Text: Tashkent State Economy University
# TSEU