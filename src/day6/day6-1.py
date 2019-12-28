with open("input.txt") as f:
    data = f.readlines()


class planet:
    def __init__(self, name):
        self.name = name
        self.orbiters = []

    def addOrbiter(self, orbiter):
        self.orbiters.append(orbiter)

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)


orbits = []
for el in data:
    orbits.append(el.split(")"))

planetList = []
for el in orbits:
    if el[0] not in planetList:
        planetList.append(planet(el[0]))
    planetList[planetList.index(el[0])].addOrbiter(el[1].strip())

orbitsQueue = ["COM"]
orbitCounter = 0
distance = 1
nextOrbit = None
while not nextOrbit == []:
    nextOrbit = []
    while not orbitsQueue == []:
        el = orbitsQueue.pop()
        if el in planetList:
            orbitCounter = orbitCounter + (planetList[planetList.index(el)].orbiters.__len__() * distance)
            nextOrbit.extend(planetList[planetList.index(el)].orbiters)
            planetList.pop(planetList.index(el))
    distance += 1
    orbitsQueue = nextOrbit
print(orbitCounter)
