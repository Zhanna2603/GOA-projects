"""https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python"""

# Find the missing letter

def find_missing_letter(chars):
    alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    for i in range(1,len(chars)):
        if alphabet [alphabet.index(chars[i])-1] != chars[i-1]:
            return [alphabet.index(chars[i])-1]
        