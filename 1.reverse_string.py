"""  
Day - 1  

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""


# reverse with slice option
def reverse_string(params):
    string=""
    for i in params[::-1]:
        string = string + i
    return string


print(reverse_string("Cat"))
print(reverse_string("The Daily Byte"))
print(reverse_string("civic"))
