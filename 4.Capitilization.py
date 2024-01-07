"""
This question is asked by Google. Given a string, return whether or 
not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false    
"""


def is_capitilized(s):
    # all letter should be cap
    # no letter should be capital
    # first letter only cap
    
    
    return s.isupper() | s.islower() | (s[0].isupper() & s[1:].islower())


print(is_capitilized("UAS"))
print(is_capitilized("coding"))
print(is_capitilized("compUter"))
print(is_capitilized("Calvin"))

    
    


