# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    msg = "It's a prime number."
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            msg = "It's not a prime number."
            break
    print(msg)

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)