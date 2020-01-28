def find_median(array):
    if len(array) % 2 == 1:
        return array[len(array)//2]
    else:
        return (array[len(array) // 2] + array[len(array) // 2 - 1]) // 2

n = int(raw_input())
x_dist = list(map(int, raw_input().split()))
frequency = list(map(int, raw_input().split()))
array = list()
for i in range(int(n)):
    array += [int(x_dist[i])] * int(frequency[i])
sorted_array = sorted(array)
array_len = len(sorted_array) // 2
iqr = float(find_median(sorted_array[ array_len + array_len % 2:]) -
            find_median(sorted_array[:array_len]))
print(iqr)
