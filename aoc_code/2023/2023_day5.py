seeds = []
maps = []
one_map = []
with open("../../test/2023/2023_day5") as f:
    content = f.readlines()
    for index, element in enumerate(content):
        if index == 0:
            element = element.strip().split()
            for seed in element[1:]:
                seeds.append(seed)
        else:
            element = element.strip().split()
            if element:
                if element[1] == "map:":
                    if one_map:
                        maps.append(one_map)
                    one_map = []
                else:
                    one_map.append((element[0], element[1], element[2]))
            if index == len(content) - 1:
                maps.append(one_map)

locations = []
for seed in seeds:
    temp = seed
    for map in maps:
        for (destination, source, length) in map:
            if int(source) <= int(temp) < int(source) + int(length):
                temp = int(temp) + int(destination) - int(source)
                break

    locations.append(temp)
print(min(locations))

seed_pairs = []
for i in range(len(seeds)):
    if i == len(seeds) - 1:
        break
    if i % 2 == 0:
        seed_pairs.append((seeds[i], seeds[i + 1]))

locations_2 = []
for start, length_seeds in seed_pairs:
    intervals = [(int(start), int(start) + int(length_seeds))]
    for map in maps:
        final_intervals = []
        for (destination, source, length) in map:
            source_end = int(source) + int(length)
            helper = []
            while intervals:
                (start_interval, end_interval) = intervals.pop()

                before_intervals = (start_interval, min(end_interval, int(source)))
                between_intervals = (max(start_interval, int(source)), min(source_end, end_interval))
                after_intervals = (max(source_end, start_interval), end_interval)
                if before_intervals[1] > before_intervals[0]:
                    helper.append(before_intervals)
                if between_intervals[1] > between_intervals[0]:
                    final_intervals.append((int(between_intervals[0]) - int(source) + int(destination),
                                            int(between_intervals[1]) - int(source) + int(destination)))
                if after_intervals[1] > after_intervals[0]:
                    helper.append(after_intervals)

            intervals = helper
        intervals = final_intervals + intervals
    locations_2.append(min(intervals)[0])
print(min(locations_2))
