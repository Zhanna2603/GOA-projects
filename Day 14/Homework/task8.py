"""8) შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი, while loop-ის გამოყენებით წაშალეთ სიის ბოლო ელემენტი იქამდე სანამ სიაში არ დარჩება ორი ელემენტი. ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია"""

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "pear", "peach", "plum", "grape"]

while len(fruits) != 2:
    fruits.pop()
print(fruits)
