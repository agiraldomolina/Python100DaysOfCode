print("Welcome to the tip calculator.\n")
total_bill = float(input("What is the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_person = int(input("How many people to split the bill? "))
total_bill_per_person= round(total_bill * (1+percentage / 100)/num_person,2)
final_amount="{:.2f}".format(total_bill_per_person)
print(f"Each person should pay: $ {final_amount}")