f = open("inputs/day2.txt", 'r')

def part_one():
    result = 0
    for line in f:
        if line[2] == 'X':
            result += 1
            if line[0] == 'A':
                result += 3
            elif line[0] == 'C':
                result += 6
        elif line[2] == 'Y':
            result += 2
            if line[0] == 'B':
                result += 3
            elif line[0] == 'A':
                result += 6
        elif line[2] == 'Z':
            result += 3
            if line[0] == 'C':
                result += 3
            elif line[0] == 'B':
                result += 6
    return result

def part_two():
    result = 0
    for line in f:
        if line[0] == 'A':
            if line[2] == 'X':
                result += 3
            if line[2] == 'Y':
                result += 4
            if line[2] == 'Z':
                result += 8
        if line[0] == 'B':
            if line[2] == 'X':
                result += 1
            if line[2] == 'Y':
                result += 5
            if line[2] == 'Z':
                result += 9
        if line[0] == 'C':
            if line[2] == 'X':
                result += 2
            if line[2] == 'Y':
                result += 6
            if line[2] == 'Z':
                result += 7
    return result

print(part_two())