sum_of_all = 0
# part 1
with open('../../test/2023/2023_day1') as f:
    contents = f.readlines()
    for row in contents:
        first = -1
        second = -1
        first_counter = False
        for element in row:
            if element.isdigit() and not first_counter:
                first_counter = True
                first = element
            if element.isdigit() and first_counter:
                second = element
        sum_of_all += int(first + second)
print(sum_of_all)


# part 2
def change(row):
    patterns = [("one", "o1e"), ("two", "t2o"), ("three", "t3e"),
                ("four", "f4r"), ("five", "f5e"), ("six", "s6x"),
                ("seven", "s7n"), ("eight", "e8t"), ("nine", "n9e")]
    for p in patterns:
        row = row.replace(*p)

    return row


sum_of_all2 = 0
with open('../../test/2023/2023_day1') as f:
    contents = f.readlines()
    for row in contents:
        first = -1
        second = -1
        first_counter = False
        row = change(row)
        for element in row:
            if element.isdigit() and not first_counter:
                first_counter = True
                first = element
            if element.isdigit() and first_counter:
                second = element
        sum_of_all2 += int(first + second)
print(sum_of_all2)
