"""9) შექმენით პროგრამა, რომელიც დაითვლის თუ რამდენჯერ შედის სიაში რიცხვი 1 numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] (ამისათვის გადაუარეთ სიას for loop-ით)"""

numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1]
count = 0
for number in numbers:
    if number == 1:
        count += 1
print(f"Number 1 appears {count} times")