print('Hello world!')

print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

print('Day 2 - Python Print Function\nHello world!')
print('Hello ' +'Alba')

print("Day 1 - String Manipulation")
print('String Concatenation is done with the \"+\" sign.')
print('e.g. print(\"Hello \" + \"world\")')
print("New lines can be created with a backslash and n.")
print(str(len(input())))

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet_name)