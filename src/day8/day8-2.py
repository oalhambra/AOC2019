with open("input.txt") as f:
    data = f.read().strip()

layers = []
while data != "":
    rows = []
    i = 0
    while i < 6:
        column = []
        j = 0
        while j < 25:
            column.append(int(data[0]))
            data = data[1:]
            j += 1
        i += 1
        rows.append(column)
    layers.append(rows)

image = [[-1 for i in range(25)] for j in range(6)]
for layer in range(layers.__len__()):
    for i in range(6):
        for j in range(25):
            if layers[layer][i][j] != 2:
                if image[i][j] == -1:
                    image[i][j] = layers[layer][i][j]

for i in range(6):
    for j in range(25):
        print(image[i][j], " ", end="")
    print()
