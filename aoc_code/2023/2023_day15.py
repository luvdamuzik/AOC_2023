from collections import defaultdict

# part1
total = 0
with open('../../test/2023/2023_day15') as f:
    contents = f.readlines()
    elements = contents[0].split(",")
    for sequence in elements:
        current = 0
        for character in sequence:
            ascii_value = ord(character) + current
            current = ascii_value * 17 % 256
        total += current
print(total)


hash_map = defaultdict(list)
with open('../../test/2023/2023_day15') as f:
    contents = f.readlines()
    elements = contents[0].split(",")
    for sequence in elements:
        current = 0
        current_string = ""
        for character in sequence:
            if character == "-":
                current_list = hash_map[current]
                for index, item in enumerate(current_list):
                    if current_string == item[:-1]:
                        current_list.pop(index)
                hash_map[current] = current_list
            elif character == "=":
                current_list = hash_map[current]
                is_in = False
                for index, item in enumerate(current_list):
                    if current_string == item[:-1]:
                        current_list[index] = current_string + sequence[-1]
                        is_in = True
                if not is_in:
                    hash_map[current].append(current_string + sequence[-1])
            else:
                ascii_value = ord(character) + current
                current = ascii_value * 17 % 256
                current_string += character

    total_2 = 0
    for value in hash_map:
        if hash_map[value]:
            for index, lens in enumerate(hash_map[value]):
                total_2 += (int(value) + 1) * (index + 1) * int(lens[-1])

print(total_2)
