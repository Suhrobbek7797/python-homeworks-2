# ' - single quote
# '' - double quote 
# \ - back slash
# / - forward slash 
# \n - newline character 
# \' - single quote
# \" - double quote 
# \t - tab
# \\ - backslash 

hello = "Hello \nW\norld"

#print(hello)


word = 'I\'m a \tteacher'
#print(word)

directorry = r"c:\vscodes\string_intro.py"
#print(type(directorry))
#print(directorry)

#         012345678910
my_str = "Hello World"  # Sequence 
#print(len(my_str))

# Slicing or Indexing
# BEGIN : END : STEP
# print(my_str[:4] + my_str[5:])
#print(my_str[::2])

#       -1012345678910
# my_str = "Hello World"  # Sequence 

#print(my_str[-5:])

# SyntaxError
# TypeError
# ValueError
# IndexError:

# Mutable vs Immutable (O'zgaruvchan vs O'zgarmas)

my_str = "Apple"
print("Oldin:", id(my_str)) 

my_str2 = 'a' + my_str[1:]
print("Keyin:", id(my_str)) 

print(my_str, my_str2)

# object.method()