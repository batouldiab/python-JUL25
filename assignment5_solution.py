#### WHILE ####

# Exercise 1:
"""
Take numeric number from user (consider that the user will submit value more than 1).
The program must print all integer numbers between 1 and the input number.
"""
number = input("Enter number more than 1 (exercise 1): ")
num = int(number)
i=1
while(i<=num):
    print(i)
    i = i + 1

# Exercise 2:
"""
Modify the previous exercise, such that it only prints even numbers between 1 and the input number.
"""
number = input("Enter number more than 1 (exercise 2): ")
num = int(number)
i=1
while(i<=num):
    if (i % 2 == 0):
        print(i)
    i = i + 1

# Exercise 3:
"""
Create a program that keeps taking inputs from user until he enters input "end".
"""
while(True):
    value = input("Enter value: ")
    if (value=="end"):
        break
    print("The value is: ", value)
print("the loop ended")


# Exercise 4
"""
The user must keep giving numbers.
when the sum of the given numbers exceed 100, 
It must stop taking values from user and write:
"Sum is more than 100".
hints:
- use infinite while loop (no for)
- while will stop when sum > 100
- sum must be initially defined as 0.
- don't forget casting for the input.
"""
print("Exercise 4:")
total = 0
while True:
    val = int(input("Enter a number: "))
    total += val
    if total > 100:
        print("Sum is more than 100")
        break


#### FOR ####
# Exercie 1:
"""
for input 4, print shape:
*
**
***
****

"""
# method 1:
num = int(input("enter number of lines"))
for i in range(num):
    for j in range(i+1):
        print("*", end=" ")
    print("\r")

# method 2:
for i in range(num):
    line = ''
    for j in range(i+1):
        line = line + '*'
    print(line)

# Exercise 2:
"""
for input 4, print shape:
   *
  ***
 *****
*******

"""
num = 4
for i in range (1, num+1):
    for j in range(num-i):
        print(" ", end="")
    for k in range(i*2-1):
        print("*", end="")
    print("\r")