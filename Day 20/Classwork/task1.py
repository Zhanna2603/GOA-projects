"""1) შექმენით ფუნქცია სახელად add რომელსაც გამოძახებისას ფრჩხილებში გადასცემთ ორ რიცხვს, ამ ფუნქციამ კი უნდა გააკეთოს არითმეტიკული ოპერაცია, კონკრეტულად შეკრება, მიღებული შედეგი კი უნდა დააბრუნოს ფუნქციამ, დაბრუნებული მნიშვნელობა შეინახეთ ცვლადში"""
#1) Создайте функцию с именем add, при вызове которой вы передаете два числа в круглых скобках, и эта функция должна выполнять арифметическую операцию, в частности сложение, и функция должна возвращать результат, сохранять возвращаемое значение в переменной.

# Example
# def greet():
#     print("Hello, Luka")
#     print("Hello, Alice")


def add(a, b):
    result = a + b
    return result 
result = add(5, 3)
print(result)