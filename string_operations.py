word = "Academy"

# Capitalize all letters in word
print("Upper Case:", word.upper())

# Lower case all letters in word
print("Lower Case:", word.lower())

# Length of a string
print("Length of String:", len(word))

# String concatenation
s1 = "String One"
s2 = "String Two"
print(s1 + " + " + s2 + " = " + (s1+s2))

# String Slicing
s = "Hello World"
print("First Letter:", s[0])
print("Last Letter:", s[-1])
print("3rd to 5th:", s[2:5])

# Searching in a string
s = "Hello"
print("Index of Letter 'o':", s.index('o'))
print("Index of Letter 'l':", s.index('l'))

# Replacing letter or word
s = "Hello World"
print("Replaced String:", s.replace("World", "There"))
