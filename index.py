import random
# Problem 1:
#
# Write some Python code that has three variables called greeting, my_name, and my_age.
# Intialize each of the 3 variables with an appropriate value,
# then rint out the example below using the 3 variables and two different approaches for formatting Strings.
#
# Using concatenation and the + and 2) Using an f-string. Sample output:
# YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!! I hear that you are YOUR_MY_AGE_VARIABLE today!

# greeting = ("Heyo")
# myName = ("Shoshard")
# myAgge = ("22")
# print(f'{greeting} {myName}!!! I hear that you are {myAgge} today!')

# Problem 2:
#
# Write some Python code that asks the user for a secret password.
# Create a loop that quits with the user's quit word. If the user doesn't enter that word, ask them to guess again.
#

# secr = ("red")
# user = ""
# while user != secr:
#     user = input("Enter the password\n")

# Problem 3:
#
#     Write some Python code using f-strings that prints 0 to 50 three times in a row (vertically).
#
# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4
# 5 5 5
#     .
#     .
#     .

# num1 = 1
# while num1 <= 50:
#     print(f'{num1} {num1} {num1}')
#     num1 += 1


#     Problem 4:
#
# Write some Python code that create a random number and stores it in a variable.
# Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit.
#

# ran = random.randint(1,10)
# user = 0
# while user != ran:
#     user = int(input("Guess the random between 1 and 10\n"))

#     Challenge
#
# Write some Python code to ask the user to create a number for the computer to guess between 1 - 10000.
# Write the code so that the computer guesses random numbers between 1 - 10000 and
# will keep guessing until the computer guesses the number correctly. Once the computer guesses the random number,
# alert the user with an alert box that displays how many guesses it took to guess the random number.

user = int(input("Enter a number between 1 and 10,000\n"))
tryies = 0

while user > 0 and user < 10001:
    ran = random.randint(1,10000)
    if ran == user:
        print("It took the computer " + str(tryies) + " tries to guess your number.")
        break
    else:
        tryies +=1