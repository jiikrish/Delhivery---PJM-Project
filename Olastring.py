print("Hello")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#Get the characters from position 5 to position 1, starting the count from the end of the string:

b = "Hello, World!"
print(b[-5:-2])

#The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Check if the phrase "ain" is present in the following text:

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))