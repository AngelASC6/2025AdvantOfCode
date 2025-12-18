import os


def calculate_position(dial, directon, amount):
    if directon == 'L':
        dial = (dial - amount) % 100

    elif directon == 'R':
        print("before: ", dial+amount)
        print("after", (dial + amount) % 100)
        dial = (dial + amount) % 100
    return dial


def unlock_safe(commands):
    dial = 50
    count = 0

    with open(commands, 'r') as file:
        for command in file:
            command = command.strip()
            if not command:
                continue
            directon = command[0]
            amount = int(command[1:])
            dial = calculate_position(dial, directon, amount)
            if dial == 0:
                count += 1
    return count


def main():
    print("code for the safe is:", unlock_safe("day1/input.txt"))


if __name__ == '__main__':
    main()