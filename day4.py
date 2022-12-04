f = open("inputs/day4.txt", 'r')
lines = f.readlines()

def part_one():
    result = 0
    for c in lines:
        c = c[:len(c) - 1]
        pairs = c.split(',')
        pair1 = pairs[0].split('-')
        pair2 = pairs[1].split('-')
        # print(c)
        if (int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1])) or (int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])):
            result += 1
    print(result)

def part_two():
    result = 0
    for c in lines:
        c = c[:len(c) - 1]
        pairs = c.split(',')
        pair1 = pairs[0].split('-')
        pair2 = pairs[1].split('-')
        # print(c)
        if int(pair1[1]) < int(pair2[0]) or int(pair1[0]) > int(pair2[1]):
            continue
        else:
            result += 1
    print(result)

part_one()
part_two()