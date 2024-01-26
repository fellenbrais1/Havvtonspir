
# Abandon for now, I don't have a good enough understanding of functions yet to make this work


def storyofyou(name='', age='', hobbies=''):
    if name == '':
        name = input("What is your name? ".capitalize())
    else:
        pass
    if age == '':
        age = input("How old are you? ") + "-years-old"
    else:
        pass
    hobbies = list(hobbies)
    if not hobbies:
        hobbies.append(input("What is your first hobby? "))
        hobbies.append(input("What is your second hobby? "))
        hobbies.append(input("What is your third hobby? "))
    else:
        pass
    print("\nYour name is", name)
    print("You are", age)
    print("Your hobbies are:")
    for item in hobbies:
        print(item)
    print("This was the story of", name)
    print("Goodbye!")


if __name__ == "__main__":
    storyofyou(name='', age='', hobbies='')

# Code not needed for now

# COMMENTED OUT FOR NOW
    # input_hobbies = []
    # input_name = input("What is your name? ".capitalize())
    # input_age = input("How old are you? ") + "-years-old"
    # input_hobbies.append(input("What is your first hobby? "))
    # input_hobbies.append(input("What is your second hobby? "))
    # input_hobbies.append(input("What is your third hobby? "))
