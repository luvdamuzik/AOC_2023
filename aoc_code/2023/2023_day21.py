from copy import deepcopy
import timeit

with open('../../test/2023/2023_day21') as f:
    contents = f.readlines()
    up_to_date_map = [[x for x in element.strip()] for element in contents]
    start = [(index, row.index("S")) for index, row in enumerate(up_to_date_map) if "S" in row]

queue = [start[0]]
#             left      right   down    up
directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]


start = timeit.default_timer()
for i in range(64):
    next_step_queue = []
    while queue:
        current = queue.pop()
        for direction in directions:
            step = (current[0] + direction[0], current[1] + direction[1])
            if up_to_date_map[step[0]][step[1]] == "." or up_to_date_map[step[0]][step[1]] == "S":
                if step not in next_step_queue:
                    next_step_queue.append(step)
    queue = deepcopy(next_step_queue)
    if i == 63:
        print(len(next_step_queue))

stop = timeit.default_timer()

print('Time: ', stop - start)
# part2 too long to brute force cant figure out a different way
