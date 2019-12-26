with open("input.txt") as f:
    data = f.read()

# instructions=list(map(int,data.split(",")))

for k in range(100):
    for j in range(100):
        regularExit = False
        instructions = list(map(int, data.split(",")))
        instructions[1] = k
        instructions[2] = j
        i = 0
        while i < instructions.__len__():
            if instructions[i] == 99:
                regularExit = True
                break
            if instructions[i] == 1:
                instructions[instructions[i + 3]] = instructions[instructions[i + 1]] + instructions[
                    instructions[i + 2]]
                i += 4
            elif instructions[i] == 2:
                instructions[instructions[i + 3]] = instructions[instructions[i + 1]] * instructions[
                    instructions[i + 2]]
                i += 4
            else:
                print("error")
                break
        if regularExit and instructions[0] == 19690720:
            print("solution:", 100 * k + j)
            exit(0)
