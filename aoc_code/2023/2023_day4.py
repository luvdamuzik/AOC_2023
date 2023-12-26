from collections import defaultdict

sum = 0
with open('../../test/2023/2023_day4') as f:
    contents = f.readlines()
    for element in contents:
        element = element.split()
        winning = set()
        still_winning = True
        value = 0
        for card in range(2, len(element)):
            if still_winning and element[card].isdigit():
                winning.add(element[card])
            elif element[card] == "|":
                still_winning = False
            elif not still_winning and element[card] in winning:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        sum += value
print(sum)

sum2 = 0
copies = defaultdict(int)
with open('../../test/2023/2023_day4') as f:
    contents = f.readlines()
    for element in contents:
        element = element.split()
        winning = set()
        still_winning = True
        value = 0
        id = int(element[1].strip(":"))
        copies[id] += 1
        for card in range(2, len(element)):
            if still_winning and element[card].isdigit():
                winning.add(element[card])
            elif element[card] == "|":
                still_winning = False
            elif not still_winning and element[card] in winning:
                value += 1

        for i in range(1, value + 1):
            copies[id + i] += 1 * copies[id]

for d in copies.values():
    sum2 += d
print(sum2)
