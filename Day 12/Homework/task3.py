"""3) შექმენით ორი ცვლადი, პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი, მეორეში კი ყველა კენტის. აიყვანეთ ორივე მე-5 ხარისხში და დაპრინტეთ ის, რომელიც არის მეტი"""

even_sum = 0
odd_sum = 0

for num in range(1, 21):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(even_sum**5)
print(odd_sum**5)