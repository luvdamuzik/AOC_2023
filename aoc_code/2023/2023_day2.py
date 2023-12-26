import re
# part1
sum = 0
with open('../../test/2023/2023_day2') as f:
    contents = f.readlines()
    for element in contents:
        element = re.split('; |: ', element)
        id = element[0].split()[1]
        counter = 1
        is_good = True
        while counter != len(element):
            game = element[counter].split(",")
            for ball in game:
                ball = ball.strip().split()
                if ball[1] == "blue" and int(ball[0]) > 14:
                    is_good = False
                elif ball[1] == "red" and int(ball[0]) > 12:
                    is_good = False
                elif ball[1] == "green" and int(ball[0]) > 13:
                    is_good = False
            counter += 1
        if is_good:
            sum += int(id)

print(sum)

# part2
sum2 = 0
with open('../../test/2023/2023_day2') as f:
    contents = f.readlines()
    for element in contents:
        element = re.split('; |: ', element)
        counter = 1
        reds = []
        greens = []
        blues = []
        while counter != len(element):
            game = element[counter].split(",")
            for ball in game:
                ball = ball.strip().split()
                if ball[1] == "blue":
                    blues.append(int(ball[0]))
                elif ball[1] == "red":
                    reds.append(int(ball[0]))
                elif ball[1] == "green":
                    greens.append(int(ball[0]))
            counter += 1

        max_reds = max(reds)
        max_greens = max(greens)
        max_blues = max(blues)
        product = max_reds * max_greens * max_blues
        sum2 += int(product)

print(sum2)