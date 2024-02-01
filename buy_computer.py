
current_choice = "-"
computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
chosen_list = []

while current_choice != '0':
    if current_choice in "12345":
        current_choice = int(current_choice)
        print("Adding {0}".format(current_choice))
        chosen_list.append(computer_parts[current_choice - 1])
    else:
        print("Please add options from the list below")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse mat")
        print("0: to finish")

    current_choice = input()

for item in chosen_list:
    print(item)
