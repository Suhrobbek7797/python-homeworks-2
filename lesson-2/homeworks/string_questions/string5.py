my_letter = input("Enter Text: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in my_letter:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Constants:", c_count)

# Answer
# Enter Text: Sukhrobbek
# This text isn't palindrome
