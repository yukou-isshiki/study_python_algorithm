data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

count_dict = {}

for number in data:
    if (number in count_dict) == False:
        count_dict[number] = 1
    else:
        count_dict[number] = count_dict[number] + 1

for k in sorted(count_dict.items()):
    for v in range(k[1]):
        print(k[0], end=" ")