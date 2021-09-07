# Use urllib.request to send network request if needed.

import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line


def codeHere():
    # Use the function to return the solution.
    count = 1
    dict1 = {}
    data = inputData.replace(' ', '')
    for i in range(1, len(data)):
        if data[i-1] == data[i]:
            count += 1
            dict1[data[i]] = count
            print("here:", i)
        else:
            count = 1

    return dict1#max(dict1.values())


print(codeHere())
''' input: 5
1 2 2 3 1'''