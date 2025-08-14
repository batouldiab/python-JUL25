# exercise:
"""
User must enter 2 values as the boudaries of a range [min_val, max_val].
then he must enter value x.
the program must print like the following:
X is in range [min_val, max_val].
or 
X is not in range [min_val, max_val].

example program:
Enter lower boundary of the range: 1
Enter upper boundary of the range: 10
Enter a value: 2
2 is in range [1, 10].
"""
min_val = int(input("Enter lower boundary of the range: "))
max_val = int(input("Enter upper boundary of the range: "))
x = int(input("Enter a value: "))
if x >= min_val and x <= max_val:
    print(f"{x} is in range [{min_val},{max_val}]")
else:
    print(f"{x} is not in range [{min_val},{max_val}]")