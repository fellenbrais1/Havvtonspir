
# A test of another way to break out of a while loop

# The loop will continue going round until one of the valid inputs is entered
available_exits = ['north', 'south', 'east', 'west']
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input('Please choose a direction: ')
    chosen_exit.casefold()
    if chosen_exit == 'quit':
        print('Game over!')
        exit()
print('Aren\'t you glad you got out of there!')

# While loops are useful when you don't know how many times the loop will have to execute in advance
# For loops are useful when you know in advance how many times a loop will have to execute

# We can also use 'break' and 'continue' to break a loop as well
