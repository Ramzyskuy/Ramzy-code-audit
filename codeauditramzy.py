data = [5, 2, 9, 1, 5, 6]

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] < data[j]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

print(data)