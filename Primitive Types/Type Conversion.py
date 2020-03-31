x = input("x: ")
y = x + 1

# The error occured because when you get input from the user its always interprested as a string.
# This would result in
y = "1" + 1

# When Python sees this expression, it doesn't know what to do
# Two different data types can't be concatenated
# Hence the error

# Type conversion to the rescue:
# int(x) <- convert to integer
# float(x) <- convert to float
# str(x) <- convert to string
# bool(x) <- convert to boolean

# Let's start again:
x = input("x: ")
print(type(x))

# Output is <class 'str'>

# Let's use type conversion here

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# Float & String conversions work in pretty much similar way

# Boolean type conversion is a bit tricky
# Because in python we have a concept of Truthy & Falsy values
# These are the values that are not exactly a Boolean True or False but
# Can be interpreted as a Boolean True or False

# List of Falsy values - These values in Boolean context are considered False
# "" <- Empty strings
# 0
# None <- Represents the absence of a value

# Anything else will be True

# Examples:
# bool(0) <- False
# bool("") <- False
# Everything else is True
# bool(1) <- True
# bool(-1) <- True
# bool(5) <- True
# Even
# bool("False") <- True







