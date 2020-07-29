import random
import timeit 


start_time = timeit.default_timer()
def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
end_time = timeit.default_timer()

data_list = random.sample(range(100), 10)
print(data_list)
print(bubble_sort(data_list))
print(end_time - start_time)


start_time2 = timeit.default_timer()
def bubble_sort(data):
    for i in range(len(data) - 1):
        swap = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            swap = True
        if swap == False:
            break
    return data
end_time2 = timeit.default_timer() 

data_list = random.sample(range(50), 10)
print(data_list)
print(bubble_sort(data_list))
print(end_time2 - start_time2)
