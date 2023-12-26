def valid(groups, current_string):
    group_index = 0
    counter = 0
    for index, spring in enumerate(current_string):
        if spring == "#":
            counter += 1
            if group_index == len(groups):
                return False
            if index == len(current_string) - 1:
                if group_index == len(groups):
                    return False
                if int(groups[group_index]) == counter:
                    group_index += 1

        elif spring == ".":
            if group_index == len(groups):
                continue
            if int(groups[group_index]) == counter:
                group_index += 1
            elif counter:
                return False
            counter = 0
    if group_index == len(groups):
        return True
    return False


count = 0


def dfs(springs, groups, current_string, index):
    if index == len(springs):
        if valid(groups, current_string):
            global count
            count += 1
        return

    if springs[index] == '?':
        dfs(springs, groups, current_string[:index] + '.' + current_string[index + 1:], index + 1)

        dfs(springs, groups, current_string[:index] + '#' + current_string[index + 1:], index + 1)

    else:
        dfs(springs, groups, current_string, index + 1)


DP = {}


def dp(springs, groups, index, block_index, current):
    key = (index, block_index, current)
    if key in DP:
        return DP[key]
    if index == len(springs):
        if block_index == len(groups) and current == 0:
            return 1
        elif block_index == len(groups) - 1 and groups[block_index] == current:
            return 1
        else:
            return 0
    answer = 0
    for c in ['.', '#']:
        if springs[index] == c or springs[index] == '?':
            if c == '.' and current == 0:
                answer += dp(springs, groups, index + 1, block_index, 0)
            elif c == '.' and current > 0 and block_index < len(groups) and groups[block_index] == current:
                answer += dp(springs, groups, index + 1, block_index + 1, 0)
            elif c == '#':
                answer += dp(springs, groups, index + 1, block_index, current + 1)
    DP[key] = answer
    return answer


with open('../../test/2023/2023_day12') as f:
    contents = f.readlines()
    ans = 0
    for element in contents:
        groups = element.split()[1].split(",")
        springs = element.split()[0]
        # part1
        dfs(springs, groups, springs, 0)
        # part2
        groups = groups + groups + groups + groups + groups
        springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
        groups = [int(x) for x in groups]

        DP.clear()
        score = dp(springs, groups, 0, 0, 0)
        ans += score

print(count)
print(ans)


