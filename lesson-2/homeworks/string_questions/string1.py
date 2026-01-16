from datetime import datetime

name = input("Enter Name: ")
birth_year = int(input("Enter Birth Year: "))

current_year = datetime.now().year
age = current_year - birth_year  

print(f"Hi {name}, you are {age} years.")

# Answer
# Enter Name: Sukhrobbek
# Enter Birth Year: 2009
# Hi Sukhrobbek, you are 17 years

