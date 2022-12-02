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

def part_one_short():
    inputs = [(ord(line[0]) - 64, ord(line[2]) - 87) for line in f]
    sum_chosen = sum(b for (a,b) in inputs)
    sum_win = sum([6 for (a,b) in inputs if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1)])
    sum_draw = sum([3 for (a,b) in inputs if a == b])
    return sum_chosen + sum_draw + sum_win

def part_two_short():
    inputs = [(ord(line[0]) - 65, ord(line[2]) - 88) for line in f]
    sum_win_draw_lose = sum(b*3 for (a,b) in inputs)
    sum_rock = sum([1 for (a,b) in inputs if (a == 0 and b == 1) or (a == 1 and b == 0) or (a == 2 and b == 2)])
    sum_paper = sum([2 for (a,b) in inputs if (a == 0 and b == 2) or (a == 1 and b == 1) or (a == 2 and b == 0)])
    sum_scissors = sum([3 for (a,b) in inputs if (a == 0 and b == 0) or (a == 1 and b == 2) or (a == 2 and b == 1)])
    return sum_win_draw_lose + sum_rock + sum_paper + sum_scissors


print(part_two_short())