# defining strings:
name = "mahdi" # double quotations can be used
name2 = 'mahdi' # single quotations can be used

print(name2)

# to define multiple lines string:
fullName = '''batoul
diab'''
fullName2 = """batoul
diab"""
print(fullName)

# length of string
word = "hello"
l = len(word)
print(l) # prints: 5
print(len(word)) # prints: 5

print(len("hello world")) # a space is considered a char # prints: 11


# selecting character by its index. remember, indices start with 0
name = "hello"
print(name[0]) # prints: h

word = 'hello'
first_char = word[0]
print(first_char) # prints: h
