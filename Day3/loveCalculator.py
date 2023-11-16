# Just for fun checking your compatibility
print("The Love Calculator is calculating your score...")
name1 = input('Name 1: ') # What is your name?
name2 = input('Name 2:') # What is their name?

# Write your code below this line 👇
names =name1.lower() + name2.lower()
timesTrue= names.count('t')+names.count('r')+names.count('u')+names.count('e')
#print(timesTrue)
timesLove= names.count('l')+names.count('o')+names.count('v')+names.count('e')
#print(timesLove)
score = int(str(timesTrue) + str(timesLove))
#print(score)
if score <10 or score >90:
    print(f"Your score is {score}, you go together like coke ar")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
