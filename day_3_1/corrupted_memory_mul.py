# Advent of Code 2024: Day 3 - Problem 1
# Corrupted Multiplying Memory
#
# Given a string of text like the following:
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# 
# We want to find the sum of all syntactically-correct "mul(x,y)" instructions
# So (2*4 + 5*5 + 11*8 + 8*5) = 161
#
# Given a text file of a bunch of these one line reports, determine
# how many reports are safe.

import os
import pathlib
from helper_functions import *

# MAIN
print("\n\nSTARTING PROGRAM...\n\n")

# Get source inputs
source_filepath = os.path.join(pathlib.Path().resolve(), "source_input.txt")
source_string = parse_source_string(source_filepath)

# Pass to helper function to calculate the number of safe reports
total = calculate_mul_sum(source_string)

# Return differential to the user
print(f"FINAL SUM: {total}")
print("\n\nENDING PROGRAM...\n\n")