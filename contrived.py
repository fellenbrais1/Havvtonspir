
# Lists are included within square brackets
numbers = [1, 45, 31, 12, 60]

# If the list contains a number divisible by 8 it will reject the numbers
for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
# This else block gives us another output if the loop runs all the way to the \
# end
# Some people don't like using 'else' like this as it can be confusing to read
# You need to watch the indentation of the else block to make sure it works in \
# the intended way
else:
    print("Those numbers are acceptable")
