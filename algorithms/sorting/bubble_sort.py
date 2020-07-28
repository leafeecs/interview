import random


def bubble_sort(data):
    for turn in range(len(data) - 1):
        swap = False
        for condition in range(len(data) - 1 - turn):
            if data[condition] > data[condition + 1]:
                data[condition], data[condition + 1] = data[condition + 1], data[condition]
                swap = True
        if swap == False:
            break
    return data

data_list = random.sample(range(100), 10)
print(data_list)                # [10, 39, 29, 54, 76, 84, 77, 53, 83, 75]
print(bubble_sort(data_list))   # [10, 29, 39, 53, 54, 75, 76, 77, 83, 84]