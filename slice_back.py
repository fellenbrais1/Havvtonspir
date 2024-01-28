
# This code contains examples of slicing using negative index values and step values
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters)

# You can use a negative step value to iterate through the values backwards, but it will miss out the first
# Value unless you program around that
backwards = letters[25:0:-1]
print(backwards)

# Slicing backwards reverses the position of the start and stop values
# Once you know this you can omit the start value to include it in the output
backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

# Programming challenge to produce the outputs 'qpo', 'edcba', and 'zyxwvuts'
# Using negative step value slices
seq_1 = letters[14:17]
rev_seq_1 = seq_1[::-1]
print("\n", rev_seq_1)

seq_2 = letters[0:5]
rev_seq_2 = seq_2[::-1]
print("\n", rev_seq_2)

seq_3 = letters[18:26]
rev_seq_3 = seq_3[::-1]
print("\n", rev_seq_3)

# OR
print("\n", letters[16:13:-1])
print("\n", letters[4::-1])
print("\n", letters[:-9:-1])

# Some slicing idioms

# This slices backwards and returns the end of the sequence according to the number
print(letters[-4:])
# This returns the last value in the string
print(letters[-1:])
# This returns the first value in the string
print(letters[:1])
# This returns the first part of the sequence up to the value's index
print(letters[:4])

# This one fails to return  result, but it will not crash the code
print(letters[:0])
