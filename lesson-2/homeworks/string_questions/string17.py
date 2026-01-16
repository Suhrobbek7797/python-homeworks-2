my_str = input("Enter Text: ")
vowels = "aeiouAEIOU"

result = ""
for ch in my_str:
    if ch in vowels:
        result += "*"
    else:
        result += ch
        print(result)

# Answer
# Enter Text: There fruits are: apples, bananas, cherries.
# Th*r* fr**ts *r*: *ppl*s, b*n*n*s, ch*rr**s.