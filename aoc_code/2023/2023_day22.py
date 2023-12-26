with open('../../test/2023/2023_day22') as f:
    contents = f.readlines()
    for element in contents:
        print(element.strip().split("~"))