# In this lesson, I am going to show you a technique for writing cleaner code

# Let's say we are wqriting an application for a University to check the eligibility

age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# We can also re-write this code as follows
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

# If you are using if-else statement to assign value to a variable then this can achieved using the following code

age = 22
message = "Eligible" if age >=18 else "Not eligible"
print(message)

# And, this is called Ternary operator
"Eligible" if age >=18 else "Not eligible"
