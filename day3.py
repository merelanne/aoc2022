f = open("inputs/day3.txt", 'r')
lines = f.readlines()

def part_one():
    result = 0
    for c in lines:
        one = c[:int(len(c)/2)]
        two = c[int(len(c)/2):len(c)-1]
        visited = []
        for a in one:
            if a in two and a not in visited:
                visited.append(a)
                if a.islower():
                    result += ord(a) - 96
                else:
                    result += ord(a) - 38
    print(result)

def part_two():
    result = 0
    index = 0
    while index < len(lines):
        a, b, c = lines[index], lines[index+1], lines[index+2]
        index += 3
        for x in a:
            if x in b and x in c:
                if x.islower():
                    result += ord(x) - 96
                else:
                    result += ord(x) - 38
                break
    print(result)

part_one()
part_two()