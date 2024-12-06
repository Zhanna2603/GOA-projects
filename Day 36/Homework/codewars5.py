"""https://www.codewars.com/kata/5648b12ce68d9daa6b000099"""

# Number of People in the Bus

def number(bus_stops):
    all_people = 0
    for i in bus_stops:
        all_people += i[0] - i[1]
    return max( all_people, 0)

# or 

# def number(bus_stops):
#     geton = 0
#     getoff = 0
    
#     for stop in bus_stops:
#         geton += stop[0]
#         getoff += stop[1]
    
#     return geton - getoff