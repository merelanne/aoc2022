f = open("inputs/day1.txt", 'r')

def part_one():
    maxsum = 0
    internalsum = 0
    for line in f:
        if line == '\n':
            if internalsum > maxsum:
                maxsum = internalsum
            internalsum = 0
        else:
            internalsum += int(line)
    if internalsum > maxsum:
        return internalsum
    return maxsum

def part_two():
    calories = []
    internalsum = 0
    for line in f:
        if line == '\n':
            calories.append(internalsum)
            internalsum = 0
        else:
            internalsum += int(line)
    calories.append(internalsum)
    calories.sort()
    return sum(calories[len(calories) - 3:])

print(part_two())