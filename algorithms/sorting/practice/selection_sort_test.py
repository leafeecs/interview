import random


def selection_sort(data):
    for i in range(len(data) - 1):
        lowest = i
        for j in range(i + 1, len(data)):
            if data[lowest] > data[j]:
                lowest = j
        data[lowest], data[i] = data[i], data[lowest]
    
    return data

data_list = random.sample(range(50), 10)
print(data_list)
print(selection_sort(data_list))