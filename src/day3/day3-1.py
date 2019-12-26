with open("input.txt") as f:
    data = f.readlines()


class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return abs(self.x) + abs(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


cable1 = data[0]
cable2 = data[1]

cable1 = cable1.split(",")
cable2 = cable2.split(",")

x = 0
y = 0
positionListCable1 = []
positionListCable2 = []
for el in cable1:
    if el.startswith('U'):
        distance = int(el.replace('U', ''))
        for i in range(distance):
            x += 1
            currPosition = position(x, y)
            positionListCable1.append(currPosition)
    if el.startswith('D'):
        distance = int(el.replace('D', ''))
        for i in range(distance):
            x -= 1
            currPosition = position(x, y)
            positionListCable1.append(currPosition)
    if el.startswith('L'):
        distance = int(el.replace('L', ''))
        for i in range(distance):
            y -= 1
            currPosition = position(x, y)
            positionListCable1.append(currPosition)
    if el.startswith('R'):
        distance = int(el.replace('R', ''))
        for i in range(distance):
            y += 1
            currPosition = position(x, y)
            positionListCable1.append(currPosition)
x = 0
y = 0
for el in cable2:
    if el.startswith('U'):
        distance = int(el.replace('U', ''))
        for i in range(distance):
            x += 1
            currPosition = position(x, y)
            positionListCable2.append(currPosition)
    if el.startswith('D'):
        distance = int(el.replace('D', ''))
        for i in range(distance):
            x -= 1
            currPosition = position(x, y)
            positionListCable2.append(currPosition)
    if el.startswith('L'):
        distance = int(el.replace('L', ''))
        for i in range(distance):
            y -= 1
            currPosition = position(x, y)
            positionListCable2.append(currPosition)
    if el.startswith('R'):
        distance = int(el.replace('R', ''))
        for i in range(distance):
            y += 1
            currPosition = position(x, y)
            positionListCable2.append(currPosition)

cableCross = set(positionListCable1).intersection(set(positionListCable2))

print(min(map(position.distance, cableCross)))
