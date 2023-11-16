# this program determines if  a particular is a leap year or not
print("Which year do you want to check?") 
year = int(input("Year: "))

# Write your code below this line 👇
if year%4 == 0 and year%100 !=0:
  print("Leap year")
elif year%4 == 0 and year%100 == 0:
  if year%400 == 0:
    print ("Leap year")
  else:
    print("Not leap year")
else:
  print("Not leap year")