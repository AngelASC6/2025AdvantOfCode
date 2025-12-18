

def calculate_position(dial, directon, amount):
    if directon == 'R':
        countUp = (dial + amount) // 100
        dial = (dial + amount) % 100
    elif directon == 'L':
        if dial == 0:
            countUp = amount // 100
        else:
            # (amount - dial) // 100 can be negative when amount < dial; clamp to 0
            countUp = max(0, (amount - dial) // 100 + (1 if amount >= dial else 0))
        dial = (dial - amount) % 100
    return dial, countUp


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
            dial, countUp = calculate_position(dial, directon, amount)
            count += countUp
    return count


def main():
    print("code for the safe is:", unlock_safe("day1/input.txt"))


if __name__ == '__main__':
    main()