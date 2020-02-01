data = "000000111111100111000000001111"

flag = list(data)[0]
count = 0
result = []
for number in list(data):
    if flag == number:
        count += 1
    else:
        result.append(count)
        count = 1
        flag = number

result.append(count)
print(result)