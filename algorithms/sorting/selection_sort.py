import random

def selection_sort(data):
    '''
    Time Comlexity: O(n^2)
    '''
    for stand_index in range(len(data) - 1):
        lowest_index = stand_index
        for index in range(stand_index + 1, len(data)):
            if data[lowest_index] > data[index]:
                lowest_index = index
        data[stand_index], data[lowest_index] = data[lowest_index], data[stand_index]

    return data

data_list = random.sample(range(100), 10)
print(data_list)                 # [22, 91, 15, 25, 49, 4, 19, 87, 32, 52]
print(selection_sort(data_list)) # [4, 15, 19, 22, 25, 32, 49, 52, 87, 91]
