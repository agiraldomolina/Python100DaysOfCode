import os
os.system("cls")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
# from art import logo  this line does the same thing as above

def caesar(text_to_transform, shift_amount, what_direction):
    transormed_text = ""
    if what_direction == 'decode':
        shift_amount = -shift_amount
    for letter in text_to_transform:
        if letter in alphabet:
            transormed_text += alphabet[(alphabet.index(letter) + shift_amount) % 26]
        else:
            transormed_text += letter
    print(f"The {what_direction}d text is {transormed_text}")

caesar_cipher_on="yes"

while caesar_cipher_on == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
 
    caesar(text_to_transform=text, shift_amount=shift, what_direction=direction)
    caesar_cipher_on = input("Type 'yes' if you want  to go again. Otherwise type 'no'.\n")

print("Goodbye 👋")

