with open('../../test/2023/2023_day16') as f:
    contents = f.readlines()
    contraption = [list(x.strip()) for x in contents]

energized_matrix = []
for x in contraption:
    row = [0 for _ in x]
    energized_matrix.append(row)

directions = {'right': (0, 1), 'left': (0, -1), 'up': (-1, 0), 'down': (1, 0)}
mirrors = {
    ('right', '/'): 'up',
    ('down', '/'): 'left',
    ('left', '/'): 'down',
    ('up', '/'): 'right',
    ('right', '\\'): 'down',
    ('up', '\\'): 'left',
    ('left', '\\'): 'up',
    ('down', '\\'): 'right'
}

counter = 0


def reset_energized_matrix(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            mat[x][y] = 0


def energized_tiles(direction, start_pos):
    global counter
    x, y = start_pos
    while 0 <= x < len(contraption) and 0 <= y < len(contraption[0]):
        if contraption[x][y] in '/\\':
            direction = mirrors[(direction, contraption[x][y])]
        # Stop loops
        if contraption[x][y] in '-|' and energized_matrix[x][y] == 1:
            return

        energized_cell = energized_matrix[x][y]
        if energized_cell == 0:
            counter += 1
            energized_matrix[x][y] = 1

        if contraption[x][y] == '|' and direction in ['left', 'right']:
            energized_tiles('up', (x - 1, y))
            energized_tiles('down', (x + 1, y))
            return
        elif contraption[x][y] == '-' and direction in ['up', 'down']:
            energized_tiles('right', (x, y + 1))
            energized_tiles('left', (x, y - 1))
            return

        x += directions[direction][0]
        y += directions[direction][1]
    else:
        return


energized_tiles('right', (0, 0))
print(counter)

# part2
total_2 = []
for i in range(len(contraption)):
    counter = 0
    reset_energized_matrix(energized_matrix)
    energized_tiles('right', (i, 0))
    total_2.append(counter)
for i in range(len(contraption)):
    counter = 0
    reset_energized_matrix(energized_matrix)
    energized_tiles('left', (i, len(contraption) - 1))
    total_2.append(counter)
for j in range(len(contraption[0])):
    counter = 0
    reset_energized_matrix(energized_matrix)
    energized_tiles('down', (0, j))
    total_2.append(counter)
for j in range(len(contraption[0])):
    counter = 0
    reset_energized_matrix(energized_matrix)
    energized_tiles('up', (len(contraption[0]) - 1, j))
    total_2.append(counter)

print(max(total_2))
# exceeded the max recursion
# def dfs(i, j, direction):
#     global counter
#     print(i, j,direction)
#     if i < 0 or i > len(contraption[0]) - 1 or j < 0 or j > len(contraption) - 1:
#         return
#     energized = energized_matrix[i][j]
#     if energized == 0:
#         counter += 1
#         energized_matrix[i][j] = 1
#
#     if contraption[i][j] == '|':
#         if direction == "right" or direction == "left":
#             dfs(i - 1, j, "up")
#             dfs(i + 1, j, "down")
#         elif direction == "up":
#             dfs(i - 1, j, "up")
#         elif direction == "down":
#             dfs(i + 1, j, "down")
#     elif contraption[i][j] == "-":
#         if direction == "up" or direction == "down":
#             dfs(i, j + 1, "right")
#             dfs(i, j - 1, "left")
#         elif direction == "right":
#             dfs(i, j + 1, "right")
#         elif direction == "left":
#             dfs(i, j - 1, "left")
#     elif contraption[i][j] == "/":
#         if direction == "up":
#             dfs(i, j + 1, "right")
#         elif direction == "down":
#             dfs(i, j - 1, "left")
#         elif direction == "left":
#             dfs(i + 1, j, "down")
#         else:
#             dfs(i - 1, j, "up")
#     elif contraption[i][j] == "\\":
#         if direction == "up":
#             dfs(i, j - 1, "left")
#         elif direction == "down":
#             dfs(i, j + 1, "right")
#         elif direction == "left":
#             dfs(i - 1, j, "up")
#         else:
#             dfs(i + 1, j, "down")
#     else:
#         if direction == "up":
#             dfs(i - 1, j, "up")
#         elif direction == "down":
#             dfs(i + 1, j, "down")
#         elif direction == "left":
#             dfs(i, j - 1, "left")
#         else:
#             dfs(i, j + 1, "right")
#

# dfs(0, 0, "right")
# print(counter)
