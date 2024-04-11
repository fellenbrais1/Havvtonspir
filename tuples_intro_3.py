# Defining tuples for different songs.

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

title, artist, year = metallica
print("Title:", title)
print("Artist:", artist)
print("Year:", year)

print("\n-------------------------------------------------------------------\n")

# Defining a new tuple with data about a coffee table.

table = (
    "Coffee",
    200,
    100,
    75,
    35.50,
)

# This code is a little difficult to read because we have to know what the /
# index values are referencing, AND get the index values right in the first /
# place.

print(table[1] * table[2])

print("\n-------------------------------------------------------------------\n")

# If we unpack the tuple using meaningful variable names, we can more easily /
# read the code and what it is doing.

name, length, width, height, price = table
print(length * width)

print("\n-------------------------------------------------------------------\n")

jukebox_songs = [
    welcome,
    bad,
    budgie,
    imelda,
    metallica,
]

for item in jukebox_songs:
    album, artist, year = item[0], item[1], item[2]
    print("Album:", album)
    print("Artist:", artist)
    print("Year:", year)
    print()

print("\n-------------------------------------------------------------------\n")

print("Albums in jukebox:", len(jukebox_songs), "\n")

for item in jukebox_songs:
    print(item[0])

print("\n-------------------------------------------------------------------\n")

# We can unpack the tuple as the for loop goes round each time.
# This loop has the advantage of also having access to the unchanged 'album'.
for album in jukebox_songs:
    album_name, album_artist, album_year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(album_name, album_artist, album_year))

print("\n-------------------------------------------------------------------\n")

# Or, we can unpack the tuples as part of the for loop.
# This type of loop is considered to be more efficient.
for album_name, album_artist, album_year in jukebox_songs:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album_name, album_artist, album_year))
