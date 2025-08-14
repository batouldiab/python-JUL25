# Assignment 4 Solution:
"""
through a while loop, 
define n = 5 
get n numeric inputs from the user (one input in each while iteration). 
if the n inputs were numeric, the program will finally print: 
“All numbers entered successfully” 
Else, if the program encounters any non-numeric value, it will directly print: 
“Invalid value entered” 
"""

i = 0
n = 5
sum = 0
while i < n:
    inp = input(f"Enter value {i+1}:")
    if inp.isnumeric() == False: # if not inp.isnumeric():
        print("invalid input!")
        break # you can instead use continue to re-ask for the value
    inpNum = int(inp)
    sum = sum + inpNum
    i = i + 1
else:
    print("All numbers entered successfully!")
    print("Sum: ", sum)

print("Out of while")