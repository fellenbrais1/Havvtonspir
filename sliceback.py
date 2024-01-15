
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters)

# you can use a negative step value to iterate through the values backwards but it will miss out the first
# value unless you program around that
backwards = letters[25:0:-1]
print(backwards)

# slicing backwards reverses the position of the start and stop values
# once you know this you can omit the start value to include it in the output
backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

# Programming challenge to produce the outputs 'qpo', 'edcba', and 'zyxwvuts'
# using negative step value slices
seq1 = letters[14:17]
revseq1 = seq1[::-1]
print("\n", revseq1)

seq2 = letters[0:5]
revseq2 = seq2[::-1]
print("\n", revseq2)

seq3 = letters[18:26]
revseq3 = seq3[::-1]
print("\n", revseq3)

#OR
print("\n", letters[16:13:-1])
print("\n", letters[4::-1])
print("\n", letters[:-9:-1])

# some slicing idioms
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[:4])

# This one fails to return  result, but it will not crash the code
print(letters[:0])
