from collections import defaultdict

# part1
schmatics = []
symbol_coords = []
neighbours = [
    (0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)
]
part_dict = defaultdict(list)
with open('../../test/2023/2023_day3') as f:
    contents = f.readlines()
    for element in contents:
        schmatics.append(element.strip())

    for x, row in enumerate(schmatics):
        for y, col in enumerate(row):
            if schmatics[x][y] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                symbol_coords.append((x, y))
    num = ""
    num_neighbours = []
    for x, row in enumerate(schmatics):
        for y, col in enumerate(row):
            if schmatics[x][y] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                num += schmatics[x][y]
                for neighbour in neighbours:
                    neighbour_x = x + neighbour[0]
                    neighbour_y = y + neighbour[1]
                    if (neighbour_x, neighbour_y) not in num_neighbours:
                        num_neighbours.append((neighbour_x, neighbour_y))
            else:
                if num:
                    for neighbour in num_neighbours:
                        if neighbour in symbol_coords:
                            part_dict[neighbour].append(int(num))
                    num = ""
                    num_neighbours.clear()

total = 0
for part in part_dict.values():
    for num in part:
        total += int(num)
print(total)

# part2
total2 = 0
for part in part_dict.values():
    if len(part) == 2:
        ratio = 1
        for num in part:
            ratio *= int(num)
        total2 += int(ratio)
print(total2)
