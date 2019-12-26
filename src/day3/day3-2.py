with open("input.txt") as f:
    data = f.readlines()


class position:
    def __init__(self, x, y, calbeLength):
        self.x = x
        self.y = y
        self.cableLength = calbeLength

    def distance(self):
        return abs(self.x) + abs(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "x:" + str(self.x) + "|y:" + str(self.y) + "|cableLength:" + str(self.cableLength)

    def __repr__(self):
        return "x:" + str(self.x) + "|y:" + str(self.y) + "|cableLength:" + str(self.cableLength)


cable1 = data[0]
cable2 = data[1]

cable1 = cable1.split(",")
cable2 = cable2.split(",")

x = 0
y = 0
cableLength = 0
positionListCable1 = []
positionListCable2 = []
for el in cable1:

    if el.startswith('U'):
        distance = int(el.replace('U', ''))
        for i in range(distance):
            cableLength += 1
            x += 1
            currPosition = position(x, y, cableLength)
            positionListCable1.append(currPosition)
    if el.startswith('D'):
        distance = int(el.replace('D', ''))
        for i in range(distance):
            cableLength += 1
            x -= 1
            currPosition = position(x, y, cableLength)
            positionListCable1.append(currPosition)
    if el.startswith('L'):
        distance = int(el.replace('L', ''))
        for i in range(distance):
            cableLength += 1
            y -= 1
            currPosition = position(x, y, cableLength)
            positionListCable1.append(currPosition)
    if el.startswith('R'):
        distance = int(el.replace('R', ''))
        for i in range(distance):
            cableLength += 1
            y += 1
            currPosition = position(x, y, cableLength)
            positionListCable1.append(currPosition)
x = 0
y = 0
cableLength = 0
for el in cable2:
    if el.startswith('U'):
        distance = int(el.replace('U', ''))
        for i in range(distance):
            cableLength += 1
            x += 1
            currPosition = position(x, y, cableLength)
            positionListCable2.append(currPosition)
    if el.startswith('D'):
        distance = int(el.replace('D', ''))
        for i in range(distance):
            cableLength += 1
            x -= 1
            currPosition = position(x, y, cableLength)
            positionListCable2.append(currPosition)
    if el.startswith('L'):
        distance = int(el.replace('L', ''))
        for i in range(distance):
            cableLength += 1
            y -= 1
            currPosition = position(x, y, cableLength)
            positionListCable2.append(currPosition)
    if el.startswith('R'):
        distance = int(el.replace('R', ''))
        for i in range(distance):
            cableLength += 1
            y += 1
            currPosition = position(x, y, cableLength)
            positionListCable2.append(currPosition)

cableCross = set(positionListCable1).intersection(set(positionListCable2))
# print(cableCross)

crossesCable1 = []
crossesCable2 = []
for el in cableCross:
    crossesCable1.append(positionListCable1[positionListCable1.index(el)])
    crossesCable2.append(positionListCable2[positionListCable2.index(el)])

combinedSteps = []
for i in range(0, crossesCable1.__len__()):
    combinedSteps.append(crossesCable1[i].cableLength + crossesCable2[i].cableLength)

# print(crossesCable1)
# print(crossesCable2)
# print(combinedSteps)
print(min(combinedSteps))

# print(min(map(position.distance, cableCross)))
