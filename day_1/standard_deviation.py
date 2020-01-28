import math


n = int(raw_input())
array = list(map(int, raw_input().split()))

# find the mean
def compute_mean(array):
    return round(sum(array)/float(n),1)

def compute_squared_distance(array, mean):
    return [(float(array[i])-float(mean))**2 for i in range(n)]

def compute_squared_sum(array):
    return sum(array)

def compute_standard_dev(sum, n):
    return math.sqrt(sum/n)

mean = compute_mean(array)
squared_distance = compute_squared_distance(array, mean)
squared_sum = compute_squared_sum(squared_distance)
std_dev = round(compute_standard_dev(squared_sum, n), 1)
print(std_dev)
