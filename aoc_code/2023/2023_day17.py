import heapq

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open('../../test/2023/2023_day17') as f:
    contents = f.readlines()
    traffic_patterns = [[int(num) for num in element.strip()] for element in contents]

# part1
def least_heat():
    queue = [(0, 0, 0, -1, -1)]
    heat = {}

    while queue:
        heat_lost, x, y, direction, step = heapq.heappop(queue)
        # print(x,y,direction,step,"QUEUE")

        if (x, y, direction, step) in heat:
            continue
        heat[(x, y, direction, step)] = heat_lost

        for i, (dx, dy) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            new_x = x + dx
            new_y = y + dy
            new_direction = i
            new_step = (1 if new_direction != direction else step + 1)

            # print(new_x,new_y,new_direction,new_step)
            if 0 <= new_x < len(traffic_patterns) and 0 <= new_y < len(traffic_patterns) and (
                    (new_direction + 2) % 4 != direction) and (new_step <= 3):
                cost = int(traffic_patterns[new_x][new_y])
                if (new_x, new_y, new_direction, new_step) in heat:
                    continue
                heapq.heappush(queue, (heat_lost + cost, new_x, new_y, new_direction, new_step))
    minimum = 10000000000
    for (x, y, direction, step), value in heat.items():
        if x == len(traffic_patterns) - 1 and y == len(traffic_patterns[0]) - 1:
            minimum = min(minimum, value)
    return minimum


print(least_heat())


# part2
def least_heat2():
    queue2 = [(0, 0, 0, -1, -1)]
    heat2 = {}

    while queue2:
        heat_lost, x, y, direction, step = heapq.heappop(queue2)
        if (x, y, direction, step) in heat2:
            continue
        heat2[(x, y, direction, step)] = heat_lost

        for i, (dx, dy) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            new_x = x + dx
            new_y = y + dy
            new_direction = i
            new_step = (1 if new_direction != direction else step + 1)

            if 0 <= new_x < len(traffic_patterns) and 0 <= new_y < len(traffic_patterns) and (
                    (new_direction + 2) % 4 != direction) and (new_step <= 10 and (new_direction == direction or step >= 4 or step == -1)):
                cost = int(traffic_patterns[new_x][new_y])
                if (new_x, new_y, new_direction, new_step) in heat2:
                    continue
                heapq.heappush(queue2, (heat_lost + cost, new_x, new_y, new_direction, new_step))

    minimum = 10000000000
    for (x, y, direction, step), value in heat2.items():
        if x == len(traffic_patterns) - 1 and y == len(traffic_patterns[0]) - 1 and step >= 4:
            minimum = min(minimum, value)
    return minimum


print(least_heat2())
