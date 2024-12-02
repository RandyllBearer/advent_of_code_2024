# Advent of Code 2024: Day 1 - Problem 2
# Lists Occurrence Similarity Score
#
# Given two equal-length lists as such:
# [9, 1, 3, 5, 6, ...]
# [10, 2, 5, 6, 4, ...]
#
# Calculate the cumulative "similarity score" between the two lists. So for each 
# integer in list_1, calculate the "similarity score" by multiplying the
# list_1 value by the # of times it occurrs in list 2. So in the above, the
# similarity_score for list_1[3] would be (5*1).

import os
import pathlib
from helper_functions import *

# MAIN
print("\n\nSTARTING PROGRAM...\n\n")

# Get source inputs
source_filepath = os.path.join(pathlib.Path().resolve(), "source_input.txt")
inputs = parse_lists(source_filepath)
master_list = inputs[0]
occurrences = inputs[1]

# Pass to helper function to calculate differentials
cumulative_similarity_score = calculate_similarity_score(master_list, occurrences)

# Return differential to the user
print(f"FINAL CUMULATIVE SIMILARITY SCORE: {cumulative_similarity_score}")
print("\n\nENDING PROGRAM...\n\n")