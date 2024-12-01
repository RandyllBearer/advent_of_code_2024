# Helper functions for AOC Day 1-1

# parse_lists opens the source_input file containing the data for the lists
# and returns them as two separate lists.
#
# file_path: The location of the source input file
# returns: [list_1, list_2] A list of lists.
def parse_lists(file_path):
    list_1 = []
    list_2 = []
    
    # Open the source_input file
    with open(file_path, "r") as file:
        for line in file:
            values = line.split()
            list_1.append(int(values[0]))
            list_2.append(int(values[1]))

    return [list_1, list_2]

# calculate_list_differential accepts two lists of equal length, sorts them,
# and index-by-index calculates the differential between each index-value.
#
# E.g. for lists [3, 1, 2] & [5, 4, 3] it becomes
# [1, 2, 3] & [3, 4, 5] and the differentials are [2, 2, 2]
# so the total is 6.
#
# list_1: A list of integers with length N
# list_2: A list of integers with length N
# returns: The cumulative differential integer
def calculate_list_differential(list_1, list_2):
    cumulative_differential = 0

    # Sort in order (ascending)
    list_1.sort()
    list_2.sort()

    # Iterate over each list
    i = 0
    while(i < len(list_1)):
        val_1 = list_1[i]
        val_2 = list_2[i]

        diff = abs(val_1 - val_2)
        cumulative_differential = cumulative_differential + diff
        i = i + 1

    return cumulative_differential