
# Experimenting with mutable objects
shopping_list = ["eggs", "cheese", "crackers", "milk", "meat"]

# After assignment, we can see that both variable's IDs are the same
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

# We can see that even after changing a variable it keeps the same ID
shopping_list.append("biscuits")

# This means that both values continue to have the same ID despite having \
# changed one of them
print()
print(id(shopping_list))
print(id(another_list))

# Experimenting with augmented assignment items to a list
shopping_list += ["ammunition for my AR-15, yee-haw!"]
print()
print(shopping_list)
print(id(shopping_list))
print(id(another_list))
