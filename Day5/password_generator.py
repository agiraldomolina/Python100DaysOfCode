#This program will generate a random password of the specified length.
import os
os.system('cls')
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
init_password = []
for char in range(nr_letters):
    init_password.append(random.choice(letters))
for char in range(nr_symbols):
    init_password += random.choice(symbols)    
for char in range(nr_numbers):
    init_password.append(random.choice(numbers))

password_length = nr_letters + nr_symbols + nr_numbers

random.shuffle(init_password)
   
print("".join(init_password))
print(len(init_password))