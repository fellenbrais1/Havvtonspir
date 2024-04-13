# Examples of escaping characters using '\'.

split_string = "This string has been \nsplit over\nseveral \nlines."
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

# Different examples of escape characters applied to string variables.
# Escape the single quotes.
print('The pet shop owner said "No, no \'e\'s uh,... he\'s only resting".')

# Or escape the double quotes.
print("The pet shop owner said \"No, no 'e's uh,... he's only resting\".")

# Or triple quotes escape everything inside them.
print("""The pet shop owner said "No, no, 'e's uh,... he's only resting".""")

# Escaping via triple quotes also allows formatting to be carried into the \
# output.
another_split_string = """This string has been
split over
several
lines."""
print(another_split_string)

# Here we escape the end of the line resulting in a non split output.
another_split_string = """This string has been \
split over \
several \
lines."""
print(another_split_string)

# Same as above.
print("""The pet shop owner said "No, no, \
'e's uh,... he's only resting".""")

# The line below won't print because it naturally contains escape chars '\'.
# 'print("C:\Users\mmccann\notes.txt")'.
print("C:\\Users\\mmccann\\notes.txt")

# We can either escape a \ with another \ or use a raw string like (r"Hello").
print(r"C:\Users\mmccann\notes.txt")
