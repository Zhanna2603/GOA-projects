"""https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python"""

# Mumbling

def accum(st):
    result =""
    for i in range(len(st)):
        result += st.upper() + st.lower()
    
    return result [:-1]