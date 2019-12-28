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

orbitChanges = ["YOU"]
changes = -2
while "SAN" not in orbitChanges:
    nextIteration = []
    for el in orbitChanges:
        if el in planetList:
            nextIteration.extend(planetList[planetList.index(el)].orbiters)
        for i in planetList:
            if el in i.orbiters:
                nextIteration.append(i.name)
    changes += 1
    orbitChanges.extend(nextIteration)
    orbitChanges = list(set(orbitChanges))
print(changes)
