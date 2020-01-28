n = raw_input()
elements = raw_input()
weights = raw_input()
int_elements = []
int_weights = []
for elem in elements.split(' '):
    int_elements.append(int(elem))
for weight in weights.split(' '):
    int_weights.append(int(weight))

result_array = list(map(lambda x: x[0]*x[1], zip(int_weights, int_elements)))
numerator = sum(result_array)
denominator = sum(int_weights)
weighted_mean = round(float(numerator/denominator),1)
print(weighted_mean)
