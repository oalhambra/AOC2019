from math import atan2

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
for i in range(data.__len__()):
    for j in range(data.__len__()):
        if data[i][j] == '#':
            angles = []
            for position in asteroidPositions:
                relative = [position[0] - i, position[1] - j]
                if relative != [0, 0]:
                    angles.append(atan2(relative[0], relative[1]))
            asteroidAngles.append(list(set(angles)))
print(max(asteroidAngles, key=lambda x: x.__len__()).__len__())

# #calculate perimeter positions:
# perimeterPositions=[]
# for i in range(data.__len__()):
#     perimeterPositions.append([0, i])
#     perimeterPositions.append([data.__len__()-1, i])
#     perimeterPositions.append([i, 0])
#     perimeterPositions.append([i, data.__len__()-1])
# perimeterPositions.remove([0, 0])
# perimeterPositions.remove([0, data.__len__()-1])
# perimeterPositions.remove([data.__len__()-1, data.__len__()-1])
# perimeterPositions.remove([data.__len__()-1, 0])
#
# visibilityList=[]
# for i in range(data.__len__()):
#     for j in range(data.__len__()):
#         if data[i][j]=='#':
#             #calculate LOS
#             # relativePositions=[]
#             # print("position", i,j)
#             visibility=0
#             for position in perimeterPositions:
#                 visible=False
#                 relative=[position[0]-i, position[1]-j]
#                 common=commonDivisors(relative[0], relative[1])
#                 # relativePositions.append([position[0]-i, position[1]-j])
#                 for el in common:
#                     if data[i+int(relative[0]/el)][j+int(relative[1]/el)]=='#':
#                         visible=True
#                     if visible:
#                         visibility+=1
#             visibilityList.append(visibility)
# print(visibilityList)
# print(max(visibilityList))
