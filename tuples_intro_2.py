# Defining different tuples, using () to make it obvious.

welcome = (
    "Welcome to my Nightmare",
    "Alice Cooper",
    1975
)
bad = (
    "Bad Company",
    "Bad Company",
    1974
)
budgie = (
    "Nightflight",
    "Budgie",
    1981
)
imelda = (
    "More Mayhem",
    "Emilda May",
    2011
)
metallica = (
    "Ride the Lightning",
    "Metallica",
    1984
)

# We can print the whole tuple.
print(metallica)

print("\n-------------------------------------------------------------------\n")

# Or we can index different values in the tuple the same as a list etc.
print(metallica[0])
print(metallica[1])
print(metallica[2])

# This code below doesn't work because tuples are immutable.

# COMMENTED OUT FOR NOW
# metallica[0] = "Master of Puppets"

print("\n-------------------------------------------------------------------\n")

# Instead, we would have to create a new list and then change items in that.
metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"

# Then we can print the new list with the changed item present.
print(metallica2)
