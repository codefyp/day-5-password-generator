#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
#creates an empty list
password_list = []

#adds to the password_list chars from letters depending on the input
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
  
#adds to the password_list chars from symbols depending on the input
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
  
#adds to the password_list chars from numbers depending on the input
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)
  
#print the list password_list
print(password_list)

#shuffle the list password_list
random.shuffle(password_list)

#print the list password_list
print(password_list)

#create a new empty string variable for the final password
password = ""

#create a loop to loop each character from the list password_list
for char in password_list:
  
#adds each character one by one from the list password_list into the empty password string variable  
  password += char

#print the final password variable
print(f"Your password is: {password}")
