# Advent of Code 2024: Day 2 - Problem 1
# Count The Number Of Safe Reports
#
# Given a report like the following:
# [1, 2, 3, 9, 10, ...]
# This report is "UNSAFE" because the numbers ascend by a value > 3
#
# [1, 2, 3, 4, 2, 3]
# This report is "UNSAFE" because the numbers ascend AND descend
#
# [1, 3, 4, 7, 8, 9]
# This report is "SAFE" because the numbers ascend in quantities <= 3
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
reports = parse_reports(source_filepath)

# Pass to helper function to calculate the number of safe reports
num_safe_reports = calculate_safe_reports(reports)

# Return differential to the user
print(f"FINAL NUMBER OF SAFE REPORTS: {num_safe_reports}")
print("\n\nENDING PROGRAM...\n\n")