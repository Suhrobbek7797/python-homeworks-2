my_text = input("Enter Text: ")
start = input("Start: ")
end = input("End: ")

if my_text.startswith(start) and my_text.endswith(end):
    print("True")
else:
    print("False")

# Answer
1()
# Enter Text: Dogs are incredibly crazy animals
# Start: Dogs
# End: animals
# True
2()
# Enter Text: Apple is fruit
# Start: Apple
# End: Vegatables
# False
