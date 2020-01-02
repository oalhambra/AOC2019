from math import atan2, pi, sqrt


def minDistance(positionList, origin):
    distances = []
    for position in positionList:
        distances.append(sqrt((position[0] - origin[0]) ** 2 + (position[1] - origin[1]) ** 2))
    return positionList[distances.index(min(distances))]


with open("input.txt") as f:
    data = f.readlines()
data = list(map(str.strip, data))

asteroidPositions = []
for i in range(data.__len__()):
    for j in range(data.__len__()):
        if data[i][j] == '#':
            asteroidPositions.append([i, j])
# iterate over # and calculate angle to other
asteroidAngles = []
asteroidAnglesWithPos = []
for i in range(data.__len__()):
    for j in range(data.__len__()):
        if data[i][j] == '#':
            angles = []
            anglesWithPos = []
            for position in asteroidPositions:
                relative = [position[0] - i, position[1] - j]
                if relative != [0, 0]:
                    angles.append(atan2(relative[0], relative[1]))
                    anglesWithPos.append([atan2(relative[0], relative[1]), position])
            asteroidAngles.append(list(set(angles)))
            asteroidAnglesWithPos.append([anglesWithPos, [i, j]])
baseSpot = asteroidAnglesWithPos[asteroidAngles.index(max(asteroidAngles, key=lambda x: x.__len__()))]

basePosition = baseSpot[1]
baseAsteroidsAngles = baseSpot[0]
aux = {}
for asteroid in baseAsteroidsAngles:
    if asteroid[0] not in aux.keys():
        aux[asteroid[0]] = [asteroid[1]]
    else:
        aux[asteroid[0]].append(asteroid[1])
angleList = list(aux.keys())
angleList.sort(reverse=False)
asteroidsDestroyed = 0
i = angleList.index(-pi / 2)
while asteroidsDestroyed < 200:
    if aux[angleList[i]] != []:
        asteroid = minDistance(aux[angleList[i]], basePosition)
        aux[angleList[i]].remove(asteroid)
        asteroidsDestroyed += 1
    i += 1
    if i % angleList.__len__() == 0:
        i = 0
print(asteroid[1] * 100 + asteroid[0])
