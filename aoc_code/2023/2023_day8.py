import re
from collections import defaultdict
from itertools import cycle
from math import lcm


def p1(inst, coord):
    counter = 0
    current = 'AAA'
    for step in cycle(inst):
        counter += 1
        current = coord[current][0] if step == 'L' else coord[current][1]
        if current == 'ZZZ':
            break
    print(counter)


def p2(instr, coord):
    current = [n for n in coord if n.endswith('A')]
    path_lengths = []
    for cur in current:
        s = 0
        for c in cycle(instr):
            s += 1
            cur = coord[cur][0] if c == 'L' else coord[cur][1]
            if cur.endswith('Z'):
                path_lengths.append(s)
                break
    print(lcm(*path_lengths))


coord = defaultdict(str)


with open('../../test/2023/2023_day8') as f:
    contents = f.readlines()
    instructions1 = contents[0].strip()
    for element in contents[2:]:
        element = re.split('= |, ', element)
        coord[element[0].strip()] = (str(element[1].strip("(")), str(element[2].strip().strip(")")))

p1(instructions1, coord)

p2(instructions1, coord)
