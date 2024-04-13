# An example of using the '.join' method.

menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
]

# Using the '.join' method below is a good way to change the output to \
# something more readable for the user, the join method connects the items in \
# the list iteration with the specified join string.

for meal in menu:
    for index in range(len(meal)-1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))

print("\n-------------------------------------------------------------------\n")

# In the below example, we are creating a list and then iterating through the \
# list as usual.

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

for flower in flowers:
    print(flower)

print("\n-------------------------------------------------------------------\n")

# This is another way to do things using '.join', first we specify the \
# seperator to be used, then we join it into the items in the iterable \
# 'flowers'. This way, '.join' handles iterating over the list by itself.

seperator = " | "
output = seperator.join(flowers)
print(output)

# '.join' is an operator for the str class, so we should feed it with a string \
# and use it to create string based outputs etc.
# All items in the iterable must be strings if we want to join the items. \
# Doing otherwise will cause the code to crash.

print("\n-------------------------------------------------------------------\n")

# This would be how you can use the '.join' method very simply.

print(", ".join(flowers))
