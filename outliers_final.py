# There may be other changes that could be made to make this program a bit \
# more user-friendly, such as specifying where a lost file should be

# Added a time measurement function, but this dataset is so small it is quite \
# buggy and sometimes equates to 0 time passed between calls of 'datetime.now()'
from datetime import datetime

print("\n* Final version (for now) of the outlier removal program")

try:
    from troubleshooting_outliers import data_1 as data
except ImportError:
    print("\nThe data could not be found, please make sure it is in the correct"
          " file location and try again.")
    # Ideally the program should specify where the data should be
    data = []
    exit()

if isinstance(data, list):
    pass
else:
    print("The data was found but appears to be of the wrong type. Please "
          "ensure the data is in list format and try again.")
    data = []
    exit()

min_valid = 100
max_valid = 200

list_to_delete = []

start_time = datetime.now()

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

end_time = datetime.now()

time_elapsed = end_time - start_time

print("Time elapsed:", time_elapsed.total_seconds())
