def part1(history):
    if all(v == 0 for v in history):
        history.append(0)
        return history[-1]
    sequence = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    part1(sequence)
    history.append(history[-1] + sequence[-1])
    return history[-1]


def part2(history):
    if all(v == 0 for v in history):
        history.append(0)
        return history[0]
    sequence = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    prev = part2(sequence)
    sequence = [prev] + sequence
    history = [history[0]-sequence[0]] + history
    return history[0]


sum1 = 0
sum2 = 0
with open('../../test/2023/2023_day9') as f:
    contents = f.readlines()
    for element in contents:
        element = [int(num) for num in element.split()]
        sum1 += part1(element)
        sum2 += part2(element)

print(sum1)
print(sum2)
