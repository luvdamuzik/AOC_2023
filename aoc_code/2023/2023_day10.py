landscape = []
start_x = 0
start_y = 0
with open('../../test/2023/2023_day10') as f:
    contents = f.readlines()
    for x, element in enumerate(contents):
        row = []
        for y, pipe in enumerate(element):
            row.append(pipe)
            if pipe == "S":
                start_x = x
                start_y = y
        landscape.append(row)

cycle = []


def valid_neighbours(x, y, land):
    pipe = land[x][y]
    if pipe == '-':
        return [(x, y - 1), (x, y + 1)]
    elif pipe == '|' or pipe == "S":
        return [(x - 1, y), (x + 1, y)]
    elif pipe == 'L':
        return [(x - 1, y), (x, y + 1)]
    elif pipe == 'J':
        return [(x - 1, y), (x, y - 1)]
    elif pipe == '7':
        return [(x + 1, y), (x, y - 1)]
    elif pipe == 'F':
        return [(x + 1, y), (x, y + 1)]


visited = []
queue = []

loop = [(start_x, start_y)]


def bfs(visit, land, s_x, s_y):
    visit.append((s_x, s_y))
    queue.append((s_x, s_y))
    while queue:
        m = queue.pop(0)

        for neighbour in valid_neighbours(m[0], m[1], land):
            if neighbour not in visit:
                visit.append(neighbour)
                queue.append(neighbour)
                loop.append(neighbour)


def inside_pre_row(x):
    horizontal = count = 0
    for y in range(len(landscape[0])):
        if (x, y) in loop and (landscape[x][y] in '|LJ' or landscape[x][y] == "S"):
            horizontal += 1
        if horizontal % 2 and (x, y) not in loop:
            count += 1
    return count


bfs(visited, landscape, start_x, start_y)
print(len(loop) // 2)
print(sum(inside_pre_row(x) for x in range(len(landscape))))
# can be done using Picks theorem and shoelace theorem use in future
