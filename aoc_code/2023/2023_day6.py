from math import sqrt, ceil

product = 1
with open('../../test/2023/2023_day6') as f:
    contents = f.readlines()
    time = contents[0].split()
    distance = contents[1].split()
    for i in range(1, len(time)):
        counter = 0
        for ms in range(int(time[i])):
            if (int(time[i]) - ms) * ms > int(distance[i]):
                counter += 1
        product *= counter
print(product)


# quadratic formula later seen
def count_ways_to_beat(time, distance):
    low = ceil(((time - sqrt(time * time - 4 * distance)) / 2))
    highd = ceil(((time + sqrt(time * time - 4 * distance)) / 2))
    high = highd
    if high == highd:
        high = high - 1
    res = high - low
    return res + 1


def binary(time, dist):
    answer = 1

    low, high = 1, (time + 1) // 2
    while high - low > 1:
        mid = (low + high) // 2
        if mid * (time - mid) > dist:
            high = mid
        else:
            low = mid

    t = high
    remaining = time - t
    answer *= (remaining - t + 1)

    return answer


time_2 = ""
distance_2 = ""
counter2 = 0
with open('../../test/2023/2023_day6') as f:
    contents = f.readlines()
    time_temp = contents[0].split()
    distance_temp = contents[1].split()
    for i in range(1, len(time_temp)):
        time_2 += "" + time_temp[i]
    for i in range(1, len(distance_temp)):
        distance_2 += "" + distance_temp[i]
    # quadratic formula(later optimization)
    # print(count_ways_to_beat(int(time_2), int(distance_2)))

    # binary search(later optimization)
    print(binary(int(time_2), int(distance_2)))

    # brute force not too long(my answer)
    # for ms in range(int(time_2)):
    #    if (int(time_2) - ms) * ms > int(distance_2):
    #        counter2 += 1
    # print(counter2)
