
try:
    from STT import STX
except ImportError:
    print("Change the name of your file to something else or check if other problems are occuring")
    exit

name = "Michael"
age = "35"
hobbies = ["Gaming", "Eating", "Programming"]

STX.story()
