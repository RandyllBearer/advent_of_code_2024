# Helper functions for AOC Day 3_1

import re
import json

# parse_source_string opens the source_input file containing the data for the reports
# and returns a string of all its contents
#
# file_path: The location of the source input file
# returns: The data in String representation
def parse_source_string(file_path):
    source_string = ""

    # Open the source_input file
    with open(file_path, "r") as file:
        source_string = file.read()

    return source_string

# calculate_mul_sum accepts a source string of data and attempts
# to sum up the total of all syntactically-correct "mul(x,y)" 
# instructions.
#
# string: The source_input String
# returns: The total sum of all valid "mul(x,y)" instructions
def calculate_mul_sum(string):
    total_sum = 0
    expression = "mul\([0-9]{1,3},[0-9]{1,3}\)"

    print("\n\n")
    print(f"string: {string}")
    print(f"expression: {expression}")
    for match in re.finditer(expression, string):
        print(f"match: {match}")

        # Strip out just the numbers from the mul command
        halves = match.group().split(",")
        first_half = halves[0].split("(")[1]
        second_half = halves[1].split(")")[0]
        print(f"first_half: {first_half}")
        print(f"second_half: {second_half}")
        value = int(first_half) * int(second_half)
        total_sum = total_sum + value

        # TODO fix why we get a match with "mul(731,2" when the last character
        # doesn't fit?

    print("\n\n")

    return total_sum