# Advent of Code 2024: Day 1 - Problem 1
# Sorted Lists Differential Comparator
#
# Given two equal-length lists as such:
# [9, 1, 3, 5, 6, ...]
# [10, 2, 5, 6, 4, ...]
#
# Sort them in order of least to greatest, and then for each index calculate
# the differential and add to a cumulative integer. Once finished with the 
# lists, present the total/cumulatie differential to the user

import os
import pathlib
from helper_functions import *

# MAIN
print("\n\nSTARTING PROGRAM...\n\n")

# Get source inputs
source_filepath = os.path.join(pathlib.Path().resolve(), "source_input.txt")
lists = parse_lists(source_filepath)
input_1 = lists[0]
input_2 = lists[1]

# QC - Ensure both lists are of same length
if(len(input_1) != len(input_2)):
    print(f"ERROR: input_1.length ({len(input_1)}) != input_2.length ({len(input_2)})")
    exit()

# Pass to helper function to calculate differentials
total_differential = calculate_list_differential(input_1, input_2)

# Return differential to the user
print(f"FINAL DIFFERENTIAL: {total_differential}")
print("\n\nENDING PROGRAM...\n\n")