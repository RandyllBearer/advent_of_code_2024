# Helper functions for AOC Day 1-2

# parse_lists opens the source_input file containing the data for the lists
# and returns them as two separate lists.
#
# file_path: The location of the source input file
# returns: [list_1, occurrences] The master list & the occurences dictionary
def parse_lists(file_path):
    list_1 = []
    occurrences = {}
    
    # Open the source_input file
    with open(file_path, "r") as file:
        for line in file:
            values = line.split()
            value_1 = int(values[0])
            value_2 = int(values[1])
            list_1.append(value_1)

            # Create key if does not exist yet
            if(occurrences.get(value_2) is None):
                occurrences[value_2] = 1
            else:
                occurrences[value_2] = occurrences[value_2] + 1

    return [list_1, occurrences]

# calculate_occurences accepts the master_list and the occurences_dictionary.
# It then iterates over the master_list, adding to the cumulative similarity_score
# using the number of occurences for each master input. E.g.:
#
# master_list = [3, 2, 3]
# occurences = {
#   3: 1,
#   2: 4
# }
#
# So we get (3*1) + (2*4) + (3*1) = similarity_score
#
# master_list: The source list to iterate over
# occurrences: The dict containing number of times a number occurred in secondary list
# returns: The cumulative similarity score
def calculate_similarity_score(master_list, occurrences):
    cumulative_similarity = 0

    # Iterate over each list
    i = 0
    while(i < len(master_list)):
        value = master_list[i]
        occurrence_value = 0
        
        if(occurrences.get(value) is None):
            occurrence_value = 0
        else:
            occurrence_value = value * occurrences[value]
        cumulative_similarity = cumulative_similarity + occurrence_value

        i = i + 1

    return cumulative_similarity