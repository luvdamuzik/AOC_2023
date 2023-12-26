image = []
original_image = []
empty_rows = []
empty_cols = []
with open('../../test/2023/2023_day11') as f:
    contents = f.readlines()
    for index, element in enumerate(contents):
        element = element.strip().split()
        if all(i == element[0][0] for i in element[0]):
            image.append(element[0])
            image.append(element[0])
            empty_rows.append(index)
        else:
            image.append(element[0])
        original_image.append(element[0])

    rotate_image = [[image[j][i] for j in range(len(image))] for i in range(len(image[0]) - 1, -1, -1)]
    rotate_original_image = [[original_image[j][i] for j in range(len(original_image))] for i in
                             range(len(original_image[0]) - 1, -1, -1)]

    new_image = []
    for element in rotate_image:
        if all(i == element[0] for i in element):
            new_image.append(element)
            new_image.append(element)
        else:
            new_image.append(element)
    for index, element in enumerate(rotate_original_image):
        if all(i == element[0] for i in element):
            empty_cols.append(139-index)


final_image = [[new_image[j][i] for j in range(len(new_image) - 1, -1, -1)] for i in range(len(new_image[0]))]


def get_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


part_1 = 0
for y_1 in range(1):
    for x_1 in range(len(final_image[0])):
        if final_image[y_1][x_1] == "#":
            for y_2 in range(len(final_image)):
                for x_2 in range(len(final_image[0])):
                    if final_image[y_2][x_2] == "#":
                        part_1 += get_manhattan_distance(x_1, y_1, x_2, y_2)

print(part_1 // 2)

part_2 = 0
part2_expansion = 1000000
for y_1 in range(len(original_image)):
    for x_1 in range(len(original_image[0])):
        if original_image[y_1][x_1] == "#":
            for y_2 in range(len(original_image)):
                for x_2 in range(len(original_image[0])):
                    if original_image[y_2][x_2] == "#":
                        if y_2 > y_1:
                            for row in range(y_1, y_2):
                                if row in empty_rows:
                                    part_2 += part2_expansion
                                else:
                                    part_2 += 1
                        if y_2 < y_1:
                            for row in range(y_2, y_1):
                                if row in empty_rows:
                                    part_2 += part2_expansion
                                else:
                                    part_2 += 1
                        if x_2 > x_1:
                            for col in range(x_1, x_2):
                                if col in empty_cols:
                                    part_2 += part2_expansion
                                else:
                                    part_2 += 1
                        if x_2 < x_1:
                            for col in range(x_2, x_1):
                                if col in empty_cols:
                                    part_2 += part2_expansion
                                else:
                                    part_2 += 1

print(part_2 // 2)
