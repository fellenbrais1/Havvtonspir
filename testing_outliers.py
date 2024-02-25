# Error testing the removing outlying data process

# -----------------------------------------------------------------------------
# Outlying values at both ends of the dataset
# PASS

print("\n* Outlying values at both ends of the dataset:")

min_valid = 100
max_valid = 200

data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

list_to_delete = []

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print("\nStop value:", stop)
for item in data[:stop]:
    list_to_delete.append(item)
del data[:stop]

start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break

print("\nStart value:", start)
for item in data[start:]:
    list_to_delete.append(item)
list_to_delete = sorted(list_to_delete)
del data[start:]

print("\nRESULTS:")
print("Cleansed data:", data)
print("Elements deleted:", list_to_delete)

# -----------------------------------------------------------------------------
# Outlying values at the low end only
# PASS

print("\n* Outlying values at the low end only:")

min_valid = 100
max_valid = 200

data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191,
]

list_to_delete = []

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print("\nStop value:", stop)
for item in data[:stop]:
    list_to_delete.append(item)
del data[:stop]

start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break

print("\nStart value:", start)
for item in data[start:]:
    list_to_delete.append(item)
list_to_delete = sorted(list_to_delete)
del data[start:]

print("\nRESULTS:")
print("Cleansed data:", data)
print("Elements deleted:", list_to_delete)

# -----------------------------------------------------------------------------
# Outlying values at the high end only
# PASS

print("\n* Outlying values at the high end only:")

min_valid = 100
max_valid = 200

data = [
    104, 105, 110, 120, 130,
    130, 150, 160, 170, 183,
    185, 187, 188, 191, 350,
    360,
]

list_to_delete = []

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print("\nStop value:", stop)
for item in data[:stop]:
    list_to_delete.append(item)
del data[:stop]

start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break

print("\nStart value:", start)
for item in data[start:]:
    list_to_delete.append(item)
list_to_delete = sorted(list_to_delete)
del data[start:]

print("\nRESULTS:")
print("Cleansed data:", data)
print("Elements deleted:", list_to_delete)

# -----------------------------------------------------------------------------
# No outlying values
# PASS

print("\n* No outlying values:")

min_valid = 100
max_valid = 200

data = [
    104, 105, 110, 120, 130,
    130, 150, 160, 170, 183,
    185, 187, 188, 191,
]

list_to_delete = []

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print("\nStop value:", stop)
for item in data[:stop]:
    list_to_delete.append(item)
del data[:stop]

start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break

print("\nStart value:", start)
for item in data[start:]:
    list_to_delete.append(item)
list_to_delete = sorted(list_to_delete)
del data[start:]

print("\nRESULTS:")
print("Cleansed data:", data)
if not list_to_delete == []:
    print("Elements deleted:", list_to_delete)
else:
    print("No elements needed to be deleted")

# -----------------------------------------------------------------------------
# Only outlying values
# PASS

print("\n* Only outlying values:")

min_valid = 100
max_valid = 200

data = [
    1, 7, 18, 25, 205,
    707, 1254, 16548, 11111111,
]

list_to_delete = []

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print("\nStop value:", stop)
for item in data[:stop]:
    list_to_delete.append(item)
del data[:stop]

start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break

print("\nStart value:", start)
for item in data[start:]:
    list_to_delete.append(item)
list_to_delete = sorted(list_to_delete)
del data[start:]

print("\nRESULTS:")
if not data == []:
    print("Cleansed data:", data)
else:
    print("Status: The entire data set was out of range and is now empty")
if not list_to_delete == []:
    print("Elements deleted:", list_to_delete)
else:
    print("No elements needed to be deleted")

# -----------------------------------------------------------------------------
# Empty data set
# PASS

print("\n* Empty data set:")

min_valid = 100
max_valid = 200

data = []

list_to_delete = []

if not data == []:
    stop = 0
    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break

    print("\nStop value:", stop)
    for item in data[:stop]:
        list_to_delete.append(item)
    del data[:stop]
    print(data)

    start = 0
    for index in range(len(data) - 1, - 1, - 1):
        if data[index] <= max_valid:
            start = index + 1
            break

    print("\nStart value:", start)
    for item in data[start:]:
        list_to_delete.append(item)
    list_to_delete = sorted(list_to_delete)
    del data[start:]

    print("\nRESULTS:")
    if not data == []:
        print("Cleansed data:", data)
    else:
        print("Status: The entire data set was out of range and is now empty")
    if not list_to_delete == []:
        print("Elements deleted:", list_to_delete)
    else:
        print("No elements needed to be deleted")
else:
    print("\nRESULTS:")
    print("Status: The data set is empty and there is nothing to process")

# -----------------------------------------------------------------------------
# Data sets including anomalous data e.g. strings,floats, Bools, etc.
# PASS

print("\n* Data sets including anomalous data e.g. strings, floats, Bools, "
      "etc.:")

min_valid = 100
max_valid = 200

data = [
    4, 5, 6.75, True, False,
    "Hello", 104, 105, 110, 120,
    130, 130, 150, 160, 170,
    183, 185, 187, 188, 191,
    301.56145, True, 350, [360, 370], "Ahoy there matey",
    380, False,
]

list_to_delete = []

if not data == []:
    stop = 0
    for index, value in enumerate(data):
        try:
            if isinstance(data[index], bool):
                stop = index
                continue
            if value >= min_valid and isinstance(value, int):
                stop = index
                break
        except TypeError:
            print("\nStatus: Dataset contains anomalous data, like strings etc."
                  " instead of numbers. There may be some issues with cleansing"
                  " the file.")
            stop = index
            continue

    print("\nStop value:", stop)
    for item in data[:stop]:
        list_to_delete.append(item)
    del data[:stop]

    start = 0
    for index in range(len(data) - 1, - 1, - 1):
        item_2 = data[index]
        try:
            if isinstance(data[index], bool):
                start = index + 1
                continue
            if data[index] <= max_valid and isinstance(data[index], int):
                start = index + 1
                break
        except TypeError:
            print("\nStatus: Dataset contains anomalous data, like strings etc."
                  " instead of numbers. There may be some issues with cleansing"
                  " the file.")
            start = index + 1
            continue

    print("\nStart value:", start)
    for item in data[start:]:
        list_to_delete.append(item)
    try:
        list_to_delete = sorted(list_to_delete)
        del data[start:]
    except TypeError:
        del data[start:]

    print("\nRESULTS:")
    if not data == []:
        print("Cleansed data:", data)
    else:
        print("Status: The entire data set was out of range and is now empty")
    if not list_to_delete == []:
        print("Elements deleted:", list_to_delete)
    else:
        print("No elements needed to be deleted")
else:
    print("\nRESULTS:")
    print("Status: The data set is empty and there is nothing to process")

# -----------------------------------------------------------------------------
# Data sets that cannot be reached
# PASS

print("\n* Data sets that cannot be reached.")

default_data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

try:
    from troubleshooting_outliers import data_2 as data
except ImportError:
    # In the real file, an exit statement would be better here, maybe also /
    # specifying to the user which directory/ position the data should be in
    print("\nThe data could not be found, please make sure it is in the correct"
          " file location and try again.")
    print("'default_data' will be used in place of 'data_2' for now.")
    data = default_data

min_valid = 100
max_valid = 200

list_to_delete = []

if not data == []:
    stop = 0
    for index, value in enumerate(data):
        try:
            if isinstance(data[index], bool):
                stop = index
                continue
            if value >= min_valid and isinstance(value, int):
                stop = index
                break
        except TypeError:
            print("\nStatus: Dataset contains anomalous data, like strings etc."
                  " instead of numbers. There may be some issues with cleansing"
                  " the file.")
            stop = index
            continue

    print("\nStop value:", stop)
    for item in data[:stop]:
        list_to_delete.append(item)
    del data[:stop]

    start = 0
    for index in range(len(data) - 1, - 1, - 1):
        item_2 = data[index]
        try:
            if isinstance(data[index], bool):
                start = index + 1
                continue
            if data[index] <= max_valid and isinstance(data[index], int):
                start = index + 1
                break
        except TypeError:
            print("\nStatus: Dataset contains anomalous data, like strings etc."
                  " instead of numbers. There may be some issues with cleansing"
                  " the file.")
            start = index + 1
            continue

    print("\nStart value:", start)
    for item in data[start:]:
        list_to_delete.append(item)
    try:
        list_to_delete = sorted(list_to_delete)
        del data[start:]
    except TypeError:
        del data[start:]

    print("\nRESULTS:")
    if not data == []:
        print("Cleansed data:", data)
    else:
        print("Status: The entire data set was out of range and is now empty")
    if not list_to_delete == []:
        print("Elements deleted:", list_to_delete)
    else:
        print("No elements needed to be deleted")
else:
    print("\nRESULTS:")
    print("Status: The data set is empty and there is nothing to process")

# -----------------------------------------------------------------------------
# Data sets containing coding keywords etc.
# FAIL
# An 'exit() statement anywhere in the list causes the program to immediately \
# terminate, not sure how to get around this one

print("\n* Data sets containing coding keywords etc.")

data = [
    4, 5, 6.75, True, False,
    "Hello", 104, 105, 110, 120,
    130, 130, 150, 160, 170,
    183, 185, 187, 188, 191,
    301.56145, True, 350, "Ahoy there matey", 360,
    False, exit(),
]

min_valid = 100
max_valid = 200

list_to_delete = []

if not data == []:
    stop = 0
    for index, value in enumerate(data):
        try:
            if isinstance(data[index], bool):
                stop = index
                continue
            if value >= min_valid and isinstance(value, int):
                stop = index
                break
        except TypeError:
            print("\nStatus: Dataset contains anomalous data, like strings etc."
                  " instead of numbers. There may be some issues with cleansing"
                  " the file.")
            stop = index
            continue

    print("\nStop value:", stop)
    for item in data[:stop]:
        list_to_delete.append(item)
    del data[:stop]

    start = 0
    for index in range(len(data) - 1, - 1, - 1):
        item_2 = data[index]
        try:
            if isinstance(data[index], bool):
                start = index + 1
                continue
            if data[index] <= max_valid and isinstance(data[index], int):
                start = index + 1
                break
        except TypeError:
            print("\nStatus: Dataset contains anomalous data, like strings etc."
                  " instead of numbers. There may be some issues with cleansing"
                  " the file.")
            start = index + 1
            continue

    print("\nStart value:", start)
    for item in data[start:]:
        list_to_delete.append(item)
    try:
        list_to_delete = sorted(list_to_delete)
        del data[start:]
    except TypeError:
        del data[start:]

    print("\nRESULTS:")
    if not data == []:
        print("Cleansed data:", data)
    else:
        print("Status: The entire data set was out of range and is now empty")
    if not list_to_delete == []:
        print("Elements deleted:", list_to_delete)
    else:
        print("No elements needed to be deleted")
else:
    print("\nRESULTS:")
    print("Status: The data set is empty and there is nothing to process")
