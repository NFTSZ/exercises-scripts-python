from random import randint

secret_number = randint(1, 100)

print(
"""
+===================================+
| Welcome to my game, fool!         |
| Enter an integer number           |
| and guess the number I’ve         |
| chosen for you.                   |
| So, what’s the secret number?     |
+===================================+
""")

while True:
    number = int(input("> "))
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        if number < secret_number:
            print("You’re not even close!")
        else:
            print("Oops!! You went a bit over.")
    else:
        print("Well done, fool! You’re free now.")
        break
