
# -----------------------------------------------------------------------------
# Data sets including anomalous data e.g. strings,floats, Bools, etc.

if __name__ == " __main__":
    print("\n   Data sets including anomalous data e.g. strings, floats, Bools,"
          " etc.:")

    min_valid = 100
    max_valid = 200

    data = [4, 5, 6.75, True, False, "Hello", 104, 105, 110, 120, 130, 130, 150,
            160, 170, 183, 185, 187, 188, 191, 301.56145, True, 350,
            "Ahoy there matey", 360, False]

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
                print("\nStatus: Dataset contains anomalous data, like strings "
                      "etc.instead of numbers. There may be some issues with "
                      "cleansing the file.")
                index += 1
                stop = index
                continue

        print("\nStop value:", stop)
        for item in data[:stop]:
            list_to_delete.append(item)
        del data[:stop]
        print(data)

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
                print(
                    "\nStatus: Dataset contains anomalous data, like strings "
                    "etc. instead of numbers. There may be some issues with "
                    "cleansing the file.")
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

        if not data == []:
            print("Cleansed data:", data)
        else:
            print(
                "Status: The entire data set was out of range and is now empty")
        if not list_to_delete == []:
            print("Elements deleted:", list_to_delete)
        else:
            print("No elements needed to be deleted")
    else:
        print("\nStatus: The data set is empty and there is nothing to process")

# --------------------------------------------------------------------------

# This list below is imported from the programs in 'testing_outliers.py'

data_1 = [4, 5, 104, 105, 110, 120, 130, 130, 150,
          160, 170, 183, 185, 187, 188, 191, 350, 360]

# This variable below is used to test if there is a TypeError when importing /
# a dataset in 'outliers_final.py'
# COMMENTED OUT FOR NOW

# data_1 = "Hello World!"

# This list below represents a broken version of 'data_2' that cannot be /
# reached by 'testing_outliers.py'

data_ = [4, 5, 104, 105, 110, 120, 130, 130, 150,
         160, 170, 183, 185, 187, 188, 191, 350, 360]
