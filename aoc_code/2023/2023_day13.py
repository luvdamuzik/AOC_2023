def horizontal_lines(matrix):
    for y in range(1, len(matrix)):
        counter_rows = 0
        counter_symetrical = 0
        for y_1 in range(y):
            if 0 <= y - y_1 - 1 and y + y_1 < len(matrix):
                counter_rows += 1
                if matrix[y - y_1 - 1] == matrix[y + y_1]:
                    counter_symetrical += 1
                else:
                    break
        if counter_symetrical == counter_rows != 0:
            return y
    return None


def horizontal_lines2(matrix):
    for y in range(1, len(matrix)):
        differences_between_rows = 0
        for y_1 in range(y):
            if 0 <= y - y_1 - 1 and y + y_1 < len(matrix):
                differences_between_rows += sum(r != l for r, l in zip(matrix[y - y_1 - 1], matrix[y + y_1]))
            if differences_between_rows > 1:
                break
        if differences_between_rows == 1:
            return y
    return None


with open('../../test/2023/2023_day13') as f:
    contents = f.readlines()
    patterns = []
    matrix = []
    for element in contents:
        element = element.split()
        if not element:
            patterns.append(matrix)
            matrix = []
        else:
            matrix.append(element[0])
    patterns.append(matrix)

    total = 0
    total_2 = 0
    for index, pattern in enumerate(patterns):

        num_hori = horizontal_lines(pattern)
        num_hori_2 = horizontal_lines2(pattern)
        if num_hori:
            total += num_hori * 100
        if num_hori_2:
            total_2 += num_hori_2 * 100

        rotated = ["".join(x) for x in zip(*pattern)]

        num_vert = horizontal_lines(rotated)
        num_vert_2 = horizontal_lines2(rotated)
        if num_vert:
            total += num_vert
        if num_vert_2:
            total_2 += num_vert_2

print(total)
print(total_2)
