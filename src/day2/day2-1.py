with open("input.txt") as f:
    data = f.read()

instructions = list(map(int, data.split(",")))

regularExit = False

instructions[1] = 12
instructions[2] = 2
i = 0
while i < instructions.__len__():
    if instructions[i] == 99:
        regularExit = True
        break
    if instructions[i] == 1:
        instructions[instructions[i + 3]] = instructions[instructions[i + 1]] + instructions[instructions[i + 2]]
        i += 4
    elif instructions[i] == 2:
        instructions[instructions[i + 3]] = instructions[instructions[i + 1]] * instructions[instructions[i + 2]]
        i += 4
    # i+=4
print(regularExit, instructions[0])
