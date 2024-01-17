
if __name__ == "__main__":
    global name
    name = ""
    global age
    age = ""
    global hobbies
    hobbies = []
    name = input("What is your name? ")
    age = input("How old are you? ") + "-years-old"
    hobbies.append(input("What is your first hobby? "))
    hobbies.append(input("What is your second hobby? "))
    hobbies.append(input("What is your third hobby? " ))


def storyofyou():
    print("Your name is", name)
    print("You are", age)
    print("Your hobbies are:")
    for item in hobbies:
        print(item)
    print("This was the story of", name)
    print("Goodbye!")


storyofyou()
