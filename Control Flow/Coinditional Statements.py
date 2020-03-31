# In almost every program, there are times when you need to make decisions,
# and that's when you use an 'If' statement

# Here is an example
temperature = 35
if temperature > 30:
    print("It's warm")    # This statement is only executed if the boolean expression in if statement evaluates to True
    print("Drink water")  # This statement is only executed if the boolean expression in if statement evaluates to True
print("Done") # <- this statement will always be executed, whether the if statement is True or not

# Notice the indentation
# These statements belong to the if statement
# We can have as many of these as we need, as long as
# these are indented

# Let's run this program now
# The output we get is
'''
It's warm
Drink water
Done
'''

# Now, if we change the temperature to 25
# The boolean expression in the if statement will now evaluate to False
# Let's check the output
'''
Done
'''
# The indented statements didn't execute as the boolena expression evaluated to False

# Introducing 'elif'
# What if you want to have multiple conditional statements
# You can use 'elif' which is then short for Else If
# So, let's add another condition to the our temperature program

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
print("Done")

# You can have as many elif statements as you want or need
# And, optionally you can have an 'else'. So, if none of the conditionals are True then what you have in the else block will be executed

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

