
# Testing the 'id()' method to generate IDs for immutable objects

# In this example, both variables have the same ID as they both evaluate \
# to 'True'
result = True
another_result = result
print(id(result))
print(id(another_result))

# Now, one will be different from the other, as 'result' is rebound to 'False'
# Boolean values are an immutable data type
result = False
print()
print(id(result))
print(id(another_result))

# The same thing but with a string, both IDs are the same
result = "Correct"
another_result = result
print()
print(id(result))
print(id(another_result))

# After reassignment to 'correct' for 'result' they will have different IDs
result = 'correct'
print()
print(id(result))

# Changing a string in any way will result in a new ID being created
result += 'ish'
print()
print(id(result))
print(id(another_result))
