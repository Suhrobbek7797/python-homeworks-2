s = input("Enter Text: ")

has_digit = False
for ch in s:
    if ch.isdigit():
        has_digit = True
print(has_digit)

# Answer
# 1()
# Enter Text: My brother is 11 years old
# True
# 2()
# Enter Text: My brother name is Asadbek
# False