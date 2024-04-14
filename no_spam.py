# An exercise to iterate through a list and remove items, also to format the \
# output of this correctly. This file includes two ways to do this.

# It will print 'MEAL OMITTED' if a meal now has no valid ingredients.

# Added a configurable 'unwanted' variable so the user can choose what \
# ingredients they want to be stripped out of the meals. This could be set up \
# as a list to strip multiple things at the same time in the future.

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

menu_2 = [
    ['egg', 'bacon', 'twinkies'],
    ['egg', 'egg', 'egg'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['spam', 'spam', 'spam', 'spam'],
    ['gravy', 'bacon', 'sausage', 'biscuits'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
]


# 'de_unwanted()' cleans spam out of the menu list and generates a new list \
# 'no_unwanted_menu' that is returned as it might be needed for something else.
def de_unwanted(
        provided_menu: list,
        unwanted_item: str
) -> list:
    """
    Scrubs instances of a specified ingredient from a menu of meal items.

    If user specified 'unwanted_item' is not in the list it will not crash.

    :param provided_menu: the provided menu of meal items.
    :param unwanted_item: the user specified item that is unneeded in the list.
    :return: 'no_unwanted_menu' is returned as a list.
    """
    no_unwanted_menu = []
    for dish in provided_menu:
        dish_string = ""
        for ingredient in dish:
            if ingredient == unwanted_item:
                continue
            else:
                dish_string += ingredient.title() + ", "
        else:
            if dish_string == "":
                no_unwanted_menu += ["MEAL OMITTED, "]
            else:
                no_unwanted_menu += [dish_string]
    else:
        for dish in no_unwanted_menu:
            print(dish)
        return no_unwanted_menu


# 'unwanted_stripper()' takes the menu as it is and prints the items without \
# whichever item is specified in 'unwanted'.
def unwanted_stripper(
        provided_menu: list,
        unwanted_item: str
) -> None:
    """
    Scrubs instances of a specified ingredient from a menu of meal items.

    If user specified 'unwanted_item' is not in the list it will not crash.

    :param provided_menu: the provided menu of meal items.
    :param unwanted_item: the user specified item that is unneeded in the list.
    :return: Function prints messages and returns 'None'.
    """
    for dish in provided_menu:
        meal_print = ""
        for ingredient in dish:
            if ingredient != unwanted_item:
                meal_print += ingredient.title() + ", "
            else:
                continue
        else:
            if meal_print == "":
                print("MEAL OMITTED, ")
            else:
                print(meal_print)


unwanted = input("Which item do you not want in your meals? \n"
                 ">>>: ")
unwanted = unwanted.casefold()

de_unwanted(menu, unwanted)

print("-----------------------------------------------------------------")

unwanted_stripper(menu, unwanted)

print("-----------------------------------------------------------------")

de_unwanted(menu_2, unwanted)

print("-----------------------------------------------------------------")

unwanted_stripper(menu_2, unwanted)

print("-----------------------------------------------------------------")

# These are the course suggested solutions for removing "spam" from the menu \
# The first iterates back through menu and deletes "spam" instances as it \
# comes across them, elegant and simple.
for meal in menu:
    for index in range(len(meal)-1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

print("-----------------------------------------------------------------")

# This second solution is similar to what is happening in 'unwanted_stripper()'\
# the print string is being modified to not print out "spam". However, this \
# solution lacks the formatting that mine has.
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()
