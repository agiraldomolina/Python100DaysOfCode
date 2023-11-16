import random
names_string=input('Enter the names separeted by commas: ')
names = names_string.split(', ')
lim_sup= len(names)
index_paying=random.randint(0,lim_sup-1)
print(f"{names[index_paying]} is going to buy the meal today!")
