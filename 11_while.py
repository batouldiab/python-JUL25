"""
While loops definition:
A while loop is used to execute a block of code repeatedly as long as a specified condition is true.
The condition is checked before the execution of the loop body.
"""

# example
x = 6

# infinite loop
# while x == 6:
#     print("inf loop")

# false condition from the beginning
while x > 10:
    print("x greater than 10")

print("out of while loop")

# simple while loop (incrementing in the loop)
print("loop 1")
i = 1
while i < 5:
    print(i)
    i = i + 1 # don't forget to increment the variable in the loop

print("out of loop 1")

# incrementing in the loop example 2
print("loop 2")
i = 1
while i < 5:
    i = i + 1 
    print(i)

print("out of loop 2")

# decrementing in the loop
print("loop 3")
i = 6
while i >= 0:
    print(i)
    i = i - 1

print("out of loop 3")

#break:
print("loop 4")
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i = i + 1

print("out of loop 4")

#continue:
print("loop 5")
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue # skip the rest of lines in the while and check condition
    print(i)

print("out of loop 5")

# else
print("loop 6")
i = 1
while i < 4:
    print(i)
    i = i + 1
else:
    print("else of while loop 6")

print("out of loop 6")

print("loop 7")
i = 1
while i < 4:
    print(i)
    i = i + 1
    if i == 2:
        break
else: # doesn't work if the break is the reason of while ending
    print("else of while loop 7")

print("out of loop 7")