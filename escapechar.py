
splitstring = "This string has been \nsplit over\nseveral \nlines"
print(splitstring)

tabbedstring = "1\t2\t3\t4\t5"
print(tabbedstring)

# different examples of escape characters applied to strings
# escape the single quotes
print('The pet shop owner said "No, no \'e\'s uh,... he\'s only resting".')
# or escape the double quotes
print("The pet shop owner said \"No, no 'e's uh,... he's only resting\".")
# or triple quotes escape everything inside them
print("""The pet shop owner said "No, no, 'e's uh,... he's only resting".""")

# escaping via triple quotes also allows formatting to be carried into the output
anothersplitstring = """This string has been
split over
several
lines"""
print(anothersplitstring)

# here we escape the end of the line resulting in a non split output
anothersplitstring = """This string has been \
split over \
several \
lines"""
print(anothersplitstring)

#same as above
print("""The pet shop owner said "No, no, \
'e's uh,... he's only resting".""")

# the line below won't print because it naturally contains escape \
# print("C:\Users\timbuchalka\notes.txt")

# we can either escape a \ with another \ or use a raw string like (r"Hello")
print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")
