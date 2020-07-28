import random

def insertion_sort(data):
    ''' 
    Time Complexity:
        Best Case: O(n^2)
        Worst Case(When it is sorted): O(n)
    '''
    for turn_index in range(len(data) - 1):
        for index in range(turn_index + 1, 0, -1):
            if data[index] < data[index - 1]:
                data[index], data[index - 1] = data[index - 1], data[index]
            else:
                break
    
    return data 

data_list = random.sample(range(100), 10)
print(data_list)                 # [24, 62, 95, 34, 10, 64, 90, 58, 18, 25]
print(insertion_sort(data_list)) # [10, 18, 24, 25, 34, 58, 62, 64, 90, 95]
