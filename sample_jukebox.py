# A sample jukebox menu selection project using data from 'jukebox_data.py'.

from jukebox_data import *

# Defining constants that should not be changed.
SONG_NUMBER = 0
SONG_TITLE = 1
SONGS_LIST = 3


# First function to choose the album.
def choose_album(initial_albums: tuple) -> tuple:
    """
    Function to allow the user to choose which album they want to play.

    Uses the 'albums' list from jukebox_data.py' to get data.

    :return: 'album' is returned as a tuple for use in 'choose_song()'.
    """
    trigger = False
    album = ""
    while not trigger:
        print("\nWelcome to the jukebox!")
        print("Please choose an album or enter '0' to quit!\n")
        album_list = []
        for item in initial_albums:
            jukebox_album = item[0]
            album_list.append(jukebox_album)
        for index, album in enumerate(album_list):
            print("{0}. {1}".format(index + 1, album))
        valid_choices = range(len(album_list))
        try:
            choice = int(input(">>>: "))
            choice -= 1
            while True:
                if choice in valid_choices:
                    album = initial_albums[choice]
                    trigger = True
                elif choice == -1:
                    print("\nExiting program!")
                    exit()
                else:
                    print("\nI am sorry, that is not a valid selection, "
                          "please try again.")
                    break
                break
        except ValueError:
            print("\nI am sorry, that is not a valid selection, "
                  "please try again.")
            continue
    else:
        return album, initial_albums


# Second function to choose the song to play.
def choose_song(
        provided_album: tuple,
        initial_albums: tuple
) -> str:
    """
    Function to allow the user to choose which song they want to play.

    Indexes into the chosen album from the 'albums' list from jukebox_data.py'
    to get data to use.

    :param provided_album: The album that was chosen in 'choose_album()'.
    :param initial_albums: The original list of imported albums.
    :return: 'track' is returned as a tuple for use in 'play_song()'.
    """
    trigger = False
    track = ""
    while not trigger:
        print("\nYou have selected:\n", provided_album[0])
        print("\nPlease choose a track or enter '0' to quit!\n")
        track_list = provided_album[SONGS_LIST]
        for track_item in track_list:
            print("{0}. {1}".format(track_item[SONG_NUMBER],
                                    track_item[SONG_TITLE]))
        valid_choices = range(len(track_list))
        try:
            choice = int(input(">>>: "))
            choice -= 1
            while True:
                if choice in valid_choices:
                    track = track_list[choice][1]
                    trigger = True
                elif choice == -1:
                    while True:
                        print("\nWould you like to choose another album? y/n?")
                        choice_2 = input(">>>: ")
                        if choice_2.casefold() == "y":
                            provided_album = choose_album(initial_albums)
                            break
                        elif choice_2.casefold() == 'n':
                            print("\nExiting program!")
                            exit()
                        else:
                            print("\nI am sorry, that is not a valid selection,"
                                  " please try again.")
                            continue
                else:
                    print("\nI am sorry, that is not a valid selection, "
                          "please try again.")
                    break
                break
        except ValueError:
            print("\nI am sorry, that is not a valid selection, "
                  "please try again.")
            continue
    else:
        return track


# Final function to play the selected song, loop around, or to finish.
def play_song(provided_track: str) -> None:
    """
    Plays the song specified by the user in 'choose_song()'.

    Uses only the track name from the tuple indexed into in 'choose_song()'.

    :param provided_track: The track chosen in 'choose_track()'.
    :return: Function prints messages and returns 'None'.
    """
    print("\nPlaying:\n", provided_track)
    while True:
        print("\nWould you like to choose another song to play? y/n")
        choice_3 = input(">>>: ")
        if choice_3.casefold() == "y":
            break
        elif choice_3.casefold() == "n":
            print("\nSee you next time!")
            exit()
        else:
            print("\nI am sorry, that is not a valid selection, "
                  "please try again.")
            continue


# Master loop to keep things going around if the user wants to play more songs.
while True:
    album_chosen = choose_album(albums)
    track_to_play = choose_song(album_chosen, albums)
    play_song(track_to_play)
