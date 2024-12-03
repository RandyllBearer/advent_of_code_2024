# Helper functions for AOC Day 1-2

# parse_reports opens the source_input file containing the data for the reports
# and returns a 2d "list of lists"
#
# file_path: The location of the source input file
# returns: [[report_1], [report_2], ...] - 2d list of lists
def parse_reports(file_path):
    reports = []
    
    # Open the source_input file
    with open(file_path, "r") as file:
        for line in file:
            str_report = line.split()
            int_report = [int(x) for x in str_report]
            reports.append(int_report)

    return reports

# determine_mode accepts two integers and returns "ASC" if the second integer
# is greater than the first and "DESC" if the second integer is smaller
# than the first
#
# value_1: an integer
# value_2: an integer
# returns: "DESC" or "ASC"
def determine_mode(value_1, value_2):
    if value_2 > value_1:
        return "ASC"
    elif value_2 < value_1:
        return "DESC"
    elif value_2 == value_1:
        return "EQUAL"

# calculate_safe_reports accepts the list of reports and determines how many
# in total are deemed "SAFE". SAFE/UNSAFE ruled as follows:
#
# All subsequent integers in a report must be ASC or DESC
# The rate of ASC or DESC must be no greater than 3
#
# Examples:
#
# [1, 2, 3, 9, 10, 11] "UNSAFE" because the numbers ascend by a value > 3
# [1, 2, 3, 4, 2, 3] "UNSAFE" because the numbers ascend AND descend
# [1, 3, 4, 7, 8, 9] "SAFE" because the numbers ascend in quantities <= 3
#
# reports: The 2d "lists of lists" containing all individual report data
# returns: The total number of "SAFE" reports
def calculate_safe_reports(reports):
    threshold = 3
    total_safe_reports = 0

    # Iterate over reports
    for report in reports:
        last_value = None
        last_mode = None
        is_safe = True

        for next_value in report:

            # Get past our first case, we can't compare it to itself
            if (last_value is None):
                last_value = next_value
                continue

            # Check if it is continuously growing or shrinking
            next_mode = determine_mode(last_value, next_value)
            if (last_mode is None):
                last_mode = next_mode
            elif (next_mode is not last_mode):
                is_safe = False
                break

            # Check if it is growing/shrinking within threshold limit
            if ((abs(next_value - last_value) > threshold) or (abs(next_value - last_value) == 0)):
                is_safe = False
                break

            last_mode = next_mode
            last_value = next_value
        
        # If it passed all checks, add to the total number of safe reports
        if (is_safe is True):
            total_safe_reports = total_safe_reports + 1

    return total_safe_reports