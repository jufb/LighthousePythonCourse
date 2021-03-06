material = "snow"
shape = "ball"
projectile = material + shape
print(projectile)

# What happens if you concatenate "firstName" to "lastName" without the space?
firstName = "Juliana"
lastName = "Borges"
fullName = firstName + " " + lastName
print(fullName)

# savory and sweet are variables containing strings; " and " is a string literal.
# Notice the spaces before and after the word "and."
# What happens if those are missing?
savory = "peanut butter"
sweet = "jelly"
sandwich = savory + " and " + sweet
print(sandwich)

# String can have built-in whitespace (\n for newline is a type of whitespace)
# Concatenation can happen inside of the print statement.
step1 = "Eat\n"
step2 = "Sleep\n"
step3 = "Code\n"
step4 = "Repeat\n"
print(step1+step2+step3+step4)

# Substrings
# The format is this: `string[start:end]`. 
# If the `end` is omitted, the returned substring will be from `start` to the end of the string. 
# If `start` is ommitted, the returned substring will be from the beginning of the string to the character just before `end`.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("The first letter of the alphabet is "+ alphabet[0] + " \nThe last letter of the alphabet is "+ alphabet[-1])
print("The first five letters of the alphabet are " + alphabet[:5])
print("The five letters in the middle of the alphabet are " + alphabet[11:16])
print("The last ten letters of the alphabet are " + alphabet[10:])

# Substring replacement
print("\nThe first actual name is: " +fullName)
differentName = fullName.replace(fullName, "Juliana Ferreira Borges")
print("I replaced as: " +differentName)
differentName2 = fullName.replace("Juliana","J")
print("I abbreviated my name as: " +differentName2)