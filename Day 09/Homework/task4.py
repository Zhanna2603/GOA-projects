"""4) შექმნით რიცხვის გამოცნობის თამაში while ციკლით, რომელიც მომხმარებელს შეეკითხება რიცხვს 1-დან 10-მდე, სანამ მომხმარებელი არ შეიყვანს თქვენთვის სასურველ რიცხვს"""

num = 7
guess =int(input("Guess a number (1-10): "))
while guess != num : 
    guess =int(input("Guess a number (1-10): "))