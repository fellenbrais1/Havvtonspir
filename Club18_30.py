
# A program to check the age of a customer is 18 to 30
# Prints a message to welcome/ dismiss based on the answer

print("Welcome to the Club 18-30 website!")
print("Let me ask you a few questions to see if a Club 18-30 holiday is the right fit for you.")
name = input("What is your name? ")
name = name.capitalize()
print("Well hello there {0}!".format(name))

# This try loop is to handle ValueError if the user types a str into the age variable
# A while loop is used to prompt the user for another input in case of an erroneous one
done = False
while not done:
    try:
        age = int(input("How old are you {0}? ".format(name)))
        if 17 < age <= 30:
            print("\nCongratulations! At {0} years old, you are eligible to come on an 18-30 holiday!".format(age))
            print("Let's get you started {0}!".format(name))
            done = True
        elif age < 18:
            print("\nI am sorry but at age {2} you are too young to join us on an 18-30 holiday!"
                  "\nPlease come back in {0} years {1}!".format(18 - age, name, age))
            done = True
        else:
            print("""\nI am sorry, but at {0} years old, you have missed your chance to join us on an 18-30 holiday!"""
                  .format(age))
            print("Please let us know if you are interested in another product {0}.".format(name))
            done = True
# This except code is what runs if an invalid input is entered
    except ValueError:
        print("Please enter your age in numbers {0}.".format(name))
