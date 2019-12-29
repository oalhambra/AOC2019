with open("input.txt") as f:
    data = f.read().strip()

layers = []
while data != "":
    rows = []
    i = 0
    while i < 25:
        column = []
        j = 0
        while j < 6:
            column.append(int(data[0]))
            data = data[1:]
            j += 1
        i += 1
        rows.append(column)
    layers.append(rows)

valueCounter = []
for layer in layers:
    zeroCount = 0
    oneCount = 0
    twoCount = 0
    for row in layer:
        for column in row:
            if column == 0:
                zeroCount += 1
            elif column == 1:
                oneCount += 1
            elif column == 2:
                twoCount += 1
    valueCounter.append([zeroCount, oneCount, twoCount])
values = min(valueCounter, key=lambda x: x[0])
print(values[1] * values[2])
