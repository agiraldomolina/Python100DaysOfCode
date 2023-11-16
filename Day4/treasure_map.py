line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
line=int(position[1])-1
letter = position[0].lower()
letters=["a","b","c"]
index_of_letter=letters.index(letter)
map[line][index_of_letter] = "X"
print(f"{line1}\n{line2}\n{line3}")