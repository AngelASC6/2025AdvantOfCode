


def find_invalid_ids(start, end):
    invalidIds = []
    for num in range(int(start), int(end)+1):
        s = str(num)
        if len(s) % 2 == 0:
            halfway = len(s) // 2
            if s[:halfway] == s[halfway:]:
                invalidIds.append(num)
    print(invalidIds)
    return invalidIds

def calculate_ids(ranges):
    range_strs = ranges.split(",")
    all_invalid = []
    for r in range_strs:
        print("range",r)
        start, end = r.split("-")
        all_invalid.extend(find_invalid_ids(start, end))
    print("/n ",all_invalid)
    invalidIdTotals = sum(all_invalid)
    return invalidIdTotals

def main():
    with open("day2/input.txt",'r') as file:
        ranges = file.read()
        print(ranges) 
    print("sum of invalid IDs is, ",calculate_ids(ranges))
main()