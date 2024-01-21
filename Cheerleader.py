
name = input("Who do you want to cheer on? ")
print()

for char in name:
    if char == " ":
        print()
    else:
        print(char, "!")
    # print("Oh yeah!")
print("\n", name, sep="")
