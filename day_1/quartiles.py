def find_median(array):
    sorted_array = sorted(array)
    n = len(sorted_array)
    if n % 2 != 0:
        middle = sorted_array[n//2]
        return float(middle, 1)
    middle = [sorted_array[int(n)//2], sorted_array[int(n)//2 - 1]]
    median = sum(middle) / 2.0
    return median


n = int(raw_input("enter the number of elements in the array: "))
array = raw_input("Enter the elements of the array: ")
int_array = [int(x) for x in array.split(' ')]
q1 = find_median(int_array[0:n//2])
print(q1)
q2 = find_median(int_array)
print(q2)
q3 = find_median(int_array[n//2+1:n])
print(q3)
