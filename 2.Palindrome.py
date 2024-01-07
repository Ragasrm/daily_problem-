"""
Ex: given strings

    "level", return true
    "algorithm", return false
    "A man, a plan, a canal: Panama.", return true
"""


import re

def valid_palindrome(str):
    new_string = re.findall('[aA-zZ]', str)
    output = ""
    for i in new_string:
        output += i
    return output.lower() == output[::-1].lower()


print(valid_palindrome("level"))
print(valid_palindrome("algorithm"))
print(valid_palindrome("A man, a plan, a canal: Panama."))
print(valid_palindrome("Borrow or rob?"))