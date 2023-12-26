from collections import defaultdict
import re
import operator

ops = {"<": operator.lt, ">": operator.gt}

workflows = defaultdict(list)
parts = []
with open('../../test/2023/2023_day19') as f:
    contents = f.readlines()
    switch = False
    for element in contents:
        if element == "\n":
            switch = True
            continue
        if not switch:
            element = re.split(',', element.strip())
            name = element[0].split("{")[0]
            workflow = [element[0].split("{")[1]]
            for i in range(1, len(element)):
                workflow.append(element[i].strip("}"))
            workflows[name] = workflow
        else:
            element = element.strip().split(",")
            values = {}
            for value in element:
                value = value.strip("}").strip("{").split("=")
                values[value[0]] = value[1]
            parts.append(values)

# part1
total = 0
for part in parts:
    current = "in"
    while current != "A" and current != "R":
        for workflow in workflows[current]:
            if ":" in workflow:
                char = workflow[0]
                operation = workflow[1]
                number = int(workflow[2:].split(":")[0])
                location = workflow[2:].split(":")[1]
                if ops[operation](int(part[char]), number):
                    current = location
                    break
            else:
                current = workflow
    if current == "A":
        total += sum(int(x) for x in part.values())

print(total)


# part2 i know the mistake just cant get my head around the recursion
total2 = 0

operator_mirror = {
    ">": "<",
    "<": ">"
}
previous = defaultdict(list)


def combinations(name, char, operation, number, x, m, a, s):
    global total2
    if name == "A":
        # print(x, m, a, s)
        # print(x * m * a * s)
        total2 += int(x * m * a * s)
        return
    if name == "R":
        return
    workflow = workflows[name]
    #print(name, workflow)
    for branch in workflow:
        #print(branch)
        if ":" in branch:
            c = branch[0]
            o = branch[1]
            n = int(branch[2:].split(":")[0])
            l = branch[2:].split(":")[1]
            if o == "<":
                if c == "s":
                    #print(l,previous[name])
                    combinations(l, c, o, n, x, m, a, n - 1)
                if c == "a":
                    #print(l,previous[name])
                    combinations(l, c, o, n, x, m, n - 1, s)
                if c == "m":
                    #print(l,previous[name])
                    combinations(l, c, o, n, x, n - 1, a, s)
                if c == "x":
                    #print(l,previous[name])
                    combinations(l, c, o, n, n - 1, m, a, s)
                if l != "A":
                    previous[name].append([c, operator_mirror[o], n - 1])
            if o == ">":
                if c == "s":
                    #print(l,previous[name])
                    combinations(l, c, o, n, x, m, a, s - n)
                if c == "a":
                    #print(l,previous[name])
                    combinations(l, c, o, n, x, m, a - n, s)
                if c == "m":
                    #print(l,previous[name])
                    combinations(l, c, o, n, x, m - n, a, s)
                if c == "x":
                    #print(l,previous[name])
                    combinations(l, c, o, n, x - n, m, a, s)
                if l != "A":
                    previous[name].append([c, operator_mirror[o], n + 1])
        else:
            #print(previous[name])
            combinations(branch, "", "", 0, x, m, a, s)


combinations("in", "", "", 0, 4000, 4000, 4000, 4000)
print(total2)
