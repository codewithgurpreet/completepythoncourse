first = "Gurpreet"
last = "Dhindsa"

# String concatenation(join) using +
full = first + " " + last
print(full)

# Formatted strings using f
full = f"{first} {last}"
print(full)

# Any valid expression can be included in the curly braces in the f string
full = f"{len(first)} {2 + 2}"
print(full)