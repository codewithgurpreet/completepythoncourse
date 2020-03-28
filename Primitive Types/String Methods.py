# Common functions available to work with strings

# len() function - length of the string
# len() function is general purpose and is not limited to strings
# later in the course we will learn about other uses
course = "Python Programming"
print(len(course))

# Remember everything in Python is an object
# And objects have functions (accuratley called as Methods)
# which we access using the . notation

# .upper() method - change everything to uppercase
print(course.upper())

# Note the method returns a new value. The original value in the
# variable is not changed.
# We can assign the new value to a variable like this

course_capital = course.upper()
print(course_capital)

# .lower() method - change everything to lowercase
print(course.lower())

# .title() method - capitalise the first letter of each word
name = "gurpreet singh dhindsa"
print(name.title())

# strip() method - remove any white space in the beginning
# and end of a string
# Particularly useful when we receive input from a user

name = "  gurpreet singh dhindsa "
print(name.strip())

# More than one method can be applied at the same time
print(name.strip().title())

# lstrip() Method - strip white space in the beginning of the string
# rstrip() Method - strip white space at the end of the string

# find() Method - find the index of a character or
# a sequence of characters in a string
course = "Python Programming"
print(course.find("r"))
print(course.find("amm"))

# Remember Python is a case sensitive language
# If a character or a sequence of characters is not found in the string
# then Python returns -1
print(course.find("pro"))
print(course.find("z"))

# replace() Method - find and replace a character or a sequence
# of characters with the new character or sequence of characters provided
course = "Python Programming"
print(course.replace("P", "J")) #replace all capital P with J

# in operator - to check for the existence of a character or
# a sequence of characters in a string
print("Pro" in course) #  Returns Boolean - True or False


# not in operator - to check for the absence of a character or
# a sequence of characters in a string
print("Java" not in course) #  Returns Boolean - True or False





