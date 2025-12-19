# I shouldve used RegEx in pt 1 T-T
import re


def find_invalid_ids(start, end):
    invalidIds = [id for id in range(int(start),int(end)) if re.match(r"^(.+)\1+$",str(id))]
    return invalidIds

def calculate_ids(ranges):
    range_strs = ranges.split(",")
    all_invalid = []
    for r in range_strs:
        start, end = r.split("-")
        all_invalid.extend(find_invalid_ids(start, end))
    invalidIdTotals = sum(all_invalid)
    return invalidIdTotals

def main():
    with open("day2/input.txt",'r') as file:
        ranges = file.read()
    print("sum of invalid IDs is, ",calculate_ids(ranges))
main()