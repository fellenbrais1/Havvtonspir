# The expression below works but is wordy and could be simplified
# 'and' is used to check that both conditions are true before returning True
age = int(input("How old are you?: "))
if age >= 16 and age <= 65:
    print("Have a good day at work.")

print("-" * 80)

# Below is an example of the same expression but simplified, so we don't need \
# to repeat the variable
if 16 <= age <= 65:
    print("Have a good day at work.")
else:
    print("Enjoy your free time.")

print("-" * 80)

# Using 'or' to check for the same things
if age < 16 or age > 65:
    print("Enjoy your free time.")
else:
    print("Have a good day at work.")

print("-" * 80)
