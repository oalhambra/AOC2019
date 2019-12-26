with open("input.txt") as f:
    data = f.read()

passwordRange = list(map(int, data.split("-")))


def twoAdjacent(password):
    valid = False
    password = str(password)
    moreThanTwo = []
    for i in range(password.__len__() - 1):
        if password[i] == password[i + 1]:
            if password[i] not in moreThanTwo:
                try:
                    if password[i] == password[i + 2]:
                        moreThanTwo.append(password[i])
                    else:
                        valid = True
                except IndexError:
                    valid = True
    return valid


def neverDecreases(password):
    valid = True
    password = str(password)
    for i in range(0, password.__len__() - 1):
        if int(password[i]) > int(password[i + 1]):
            valid = False
    return valid


possiblePassword = []
for password in range(passwordRange[0], passwordRange[1]):
    if twoAdjacent(password) and neverDecreases(password):
        possiblePassword.append(password)

print(len(possiblePassword))
