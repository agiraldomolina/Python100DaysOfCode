print('Hi to the rollercoaster!')
height = int(input('What is your height in cm? '))
bill =0
if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age in years? '))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    wants_photo = input('Would you like a photo? Y or N? ')
    if wants_photo == "Y":
        bill += 3
    if age >=45 and age <=55:
        bill =0
    print(f'Your bill is ${bill}')
else:
    print('Sorry, you have to grow taller before you can ride!')