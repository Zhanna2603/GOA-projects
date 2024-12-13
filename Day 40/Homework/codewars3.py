"""https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python"""

# Find the missing letter

def find_missing_letter(chars):
    for i in range(len(chars)- 1):
        if ordered(chars [i+1]) != ordered(chars [i])+1:
            return ordered(chars [i])+1
        