from jukebox_data import *

print("Welcome to the jukebox!")
print("Please choose an album! (Invalid choice exits)")
album_list = []
for item in albums:
    jukebox_album = item[0]
    album_list.append(jukebox_album)
for index, album in enumerate(album_list):
    print("{0}. {1}".format(index + 1, album))
valid_choices = range(len(album_list))
choice = int(input(">>>: "))
choice -= 1
while True:
    if choice in valid_choices:
        album = albums[choice]
        break
    else:
        print("Invalid choice, exiting the program.")
        exit()
print("You have selected:", album[0])
print("Please choose a track! (Invalid choice exits)")
track_list = album[3]
for track_item in track_list:
    print("{0}. {1}".format(track_item[0], track_item[1]))
valid_choices = range(len(track_list))
choice = int(input(">>>: "))
choice -= 1
while True:
    if choice in valid_choices:
        track = track_list[choice][1]
        break
    else:
        print("Invalid choice, exiting the program.")
        exit()
print("Playing:", track)
