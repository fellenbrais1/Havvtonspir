# The final comma on a list allows a new item to be added to the list without \
# throwing up an error

# This also allows elements in a list to be rearranged without incident
# Use [Alt + Shift + Up/ Down] to do this while hovering over the line you \
# want to move

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

for meal in menu:
    if "spam" not in meal:
        print(meal)
        print("contains:")
        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of: {1}"
              .format(meal, meal.count("spam")))
