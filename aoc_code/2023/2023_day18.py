def polyarea(x, y):
    area = 0
    for i in range(len(x) - 1):
        x1 = x[i]
        y1 = y[i]
        x2, y2 = x[i + 1], y[i + 1]
        area += x1 * y2 - x2 * y1
    return area


with open('../../test/2023/2023_day18') as f:
    contents = f.readlines()
    instructions = [element.strip().split() for element in contents]

directions = {
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1)
}

direction_map = {
    0: "R",
    1: "D",
    2: "L",
    3: "U"
}
current = (0, 0)
dug_up_coords = set()
dug_up_coords.add(current)
x_coords = []
y_coords = []
boundary_count = 0

current_2 = (0, 0)
boundary_count_2 = 0
x_coords_2 = []
y_coords_2 = []

for instruction in instructions:
    direction = instruction[0]
    step = int(instruction[1])
    color = instruction[2].strip("(#").rstrip(")")
    direction_2 = direction_map[int(color[-1])]
    step_2 = int(color[:-1], 16)
    # brute force part1
    for i in range(step):
        current = (current[0] + directions[direction][0], current[1] + directions[direction][1])
        dug_up_coords.add(current)
        boundary_count += 1

    x_coords.append(current[1])
    y_coords.append(current[0])

    # part2
    current_2 = (
        current_2[0] + (step_2 * directions[direction_2][0]), current_2[1] + (step_2 * directions[direction_2][1]))
    x_coords_2.append(current_2[1])
    y_coords_2.append(current_2[0])
    boundary_count_2 += step_2

# thank you day 10 XD
area = polyarea(x_coords, y_coords) // 2
# Picks Theorem A = i + b/2 -1
i = area - (boundary_count / 2) + 1
print(i + boundary_count)

area_2 = abs(polyarea(x_coords_2, y_coords_2)) // 2
i_2 = area_2 - (boundary_count_2 / 2) + 1
print(i_2 + boundary_count_2)
