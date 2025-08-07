num = input("Enter a number: ")
print(num)
print(type(num))

res = int(num)*2
print(res)

# Exercise:
"""
Get a number or string from user.
Print if it's numeric (True or False).
(witout casting)
"""
value = input("Enter anything: ")
numeric = value.isnumeric()
print(numeric)


# Exercise 2:
"""
Create list cars that looks like:
[ {"brand": "ford", "year":2024}, {"brand": "Toyota", "year":2022}]
contains 2 dicts. each containing brand and year information.
the values must be taken from the USER
"""
# method 1:

b = input("Brand: ")
y = input("Year: ")
y_num = int(y)
car1 = { "brand": b, "year": y_num}

b = input("Brand: ")
y = input("Year: ")
y_num = int(y)
car2 = { "brand": b, "year": y_num}

lst = [car1,  car2]
print(lst)

# method 2: (with single input like: toyota,2020,mazda,2008)
input = input("Enter the input string (example: toyota,2020,mazda,2008): ")
splitted_txt = input.split(",")
car1 = {
    "Brand": splitted_txt[0],
    "Year": splitted_txt[1]
}
car2 = {
    "Brand": splitted_txt[2],
    "Year": splitted_txt[3]
}
cars = [car1, car2]
print(cars)

# method 3: (with multiple inputs)
carsList = [
    {
        "brand": input("Enter the brand (car1): "),
        "year": input("Enter the year (car1): ")
    },
    {
         "brand": input("Enter the brand (car2): "),
        "year": input("Enter the year (car2): ")
    }
]
print(carsList)