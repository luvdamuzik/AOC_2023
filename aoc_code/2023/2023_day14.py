from collections import defaultdict
from copy import deepcopy

# part1
total = 0
col_max = defaultdict(int)
with open('../../test/2023/2023_day14') as f:
    contents = f.readlines()
    num_of_rows = len(contents)
    for index, element in enumerate(contents):
        for index1, space in enumerate(element):
            if index == 0:
                if space == ".":
                    col_max[index1] = num_of_rows
                if space == "#":
                    col_max[index1] = num_of_rows - 1
                if space == "O":
                    col_max[index1] = num_of_rows - 1
                    total += num_of_rows
            else:
                if space == ".":
                    continue
                if space == "#":
                    col_max[index1] = num_of_rows - index - 1
                if space == "O":
                    total += col_max[index1]
                    col_max[index1] = col_max[index1] - 1

print(total)


def cycle(mat):
    num_of_rows_2 = len(mat)
    for i in range(4):
        col_max = defaultdict(int)
        for x, row in enumerate(mat):
            for y, col in enumerate(row):
                if x == 0:
                    if col == ".":
                        col_max[y] = num_of_rows_2
                    if col == "#":
                        col_max[y] = num_of_rows_2 - 1
                    if col == "O":
                        col_max[y] = num_of_rows_2 - 1
                else:
                    if col == ".":
                        continue
                    if col == "#":
                        col_max[y] = num_of_rows_2 - x - 1
                    if col == "O":
                        mat[x][y] = "."
                        mat[num_of_rows_2 - col_max[y]][y] = "O"
                        col_max[y] = col_max[y] - 1

        mat = [list(z) for z in zip(*mat[::-1])]
    return mat


matrix = []
# part2
with open('../../test/2023/2023_day14') as f:
    contents = f.readlines()
    for element in contents:
        matrix.append([x for x in element.strip()])

previous_matrices = [matrix]
first_matrix_cycle = []
for i in range(1000000000):
    current_matrix = deepcopy(previous_matrices[i])
    next_matrix = cycle(current_matrix)
    if next_matrix in previous_matrices:
        first_matrix_cycle = next_matrix
        break
    else:
        previous_matrices.append(next_matrix)

start_of_cycle = previous_matrices.index(first_matrix_cycle)
length_of_cycle = len(previous_matrices) - start_of_cycle
# need (1000000000 - start) % length -th of the cycle
# in example I need 4th element of the cycle which starts at 3 so I need the 6th element of prev_mat
billion_cycle = start_of_cycle + (1000000000 - start_of_cycle) % length_of_cycle

matrix_cycle = previous_matrices[billion_cycle]

num_row_last = len(matrix_cycle)
total_last = 0

for x, row in enumerate(matrix_cycle):
    for y, col in enumerate(row):
        if col == "O":
            total_last += num_row_last - x

print(total_last)
