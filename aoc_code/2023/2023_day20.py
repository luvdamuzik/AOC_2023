from collections import defaultdict
from math import lcm

flip_flops = defaultdict(list)
conjucations = defaultdict(list)
broadcaster = []

flip_flop_mirror = {
    "off": "on",
    "on": "off"
}

conjucations_mirror = {
    "high": "low",
    "low": "high"
}


def flip_flop(module, signal):
    if signal == "high":
        return
    else:
        current_state = flip_flops[module][1]
        flip_flops[module][1] = flip_flop_mirror[flip_flops[module][1]]
        if current_state == "off":
            return "high"
        if current_state == "on":
            return "low"


def conjucation(name):
    for module in flip_flops:
        if name in flip_flops[module][0]:
            if flip_flops[module][1] == "off":
                return "high"
    for module in conjucations:
        if name in conjucations[module][0]:
            if conjucations[module][1] == "low":
                return "high"

    return "low"


cycle_len = []


def button(i):
    queue = []
    signal = "low"
    for module in broadcaster:
        queue.append([module, signal])
    high_counter = 0
    low_counter = 0
    while queue:
        current = queue.pop(0)

        if current[0] == "rx" and current[1] == "low":
            return
        if current[0] in ["qz", "cq", "jx", "tt"] and current[1] == "high":
            cycle_len.append(i)

        if current[0] in flip_flops:
            if not current[1]:
                continue
            if current[1] == "high":
                high_counter += 1
            if current[1] == "low":
                low_counter += 1
            sending = flip_flop(current[0], current[1])
            for add in flip_flops[current[0]][0]:
                queue.append([add, sending, current[0]])
                if add not in flip_flops and add not in conjucations:
                    if sending == "high":
                        high_counter += 1
                    if sending == "low":
                        low_counter += 1
                    continue

        if current[0] in conjucations:
            if not current[1]:
                continue
            if current[1] == "high":
                high_counter += 1
            if current[1] == "low":
                low_counter += 1
            sending = conjucation(current[0])
            for add in conjucations[current[0]][0]:
                if add in conjucations:
                    conjucations[current[0]][1] = sending
                    queue.append([add, conjucation(add), current[0]])
                else:
                    queue.append([add, sending, current[0]])
                if add not in flip_flops and add not in conjucations:
                    if sending == "high":
                        high_counter += 1
                    if sending == "low":
                        low_counter += 1
                    continue
    return high_counter, low_counter + 1


with open('../../test/2023/2023_day20') as f:
    contents = f.readlines()
    for element in contents:
        if "&" in element or "%" in element:
            element = element.strip().split()
            name = element[0][1:]
            destinations = [x.strip(",") for x in element[2:]]
            if "%" in element[0]:
                flip_flops[name] = [destinations, "off"]
            if "&" in element[0]:
                conjucations[name] = [destinations, "low"]
        else:
            element = element.strip().split()
            destinations = [x.strip(",") for x in element[2:]]
            broadcaster = destinations

# part1
high_counter_total = 0
low_counter_total = 0
for i in range(1000):
    high_counter, low_counter = button(i)
    high_counter_total += high_counter
    low_counter_total += low_counter
print(low_counter_total * high_counter_total)

# part2
# 1001st cycle starts here
for i in range(1001,1000000000000000000000000):
    if len(cycle_len) == 4:
        break
    button(i)
print(lcm(*cycle_len))
