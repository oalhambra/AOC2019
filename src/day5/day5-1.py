class Intcode:
    def __init__(self, instructions):
        self.instructions = instructions

    def interpreter(self, index, args=[]):
        instruction = self.instructions[index] % 100
        mode = int(self.instructions[index] / 100)

        if instruction == 99:
            return [-1]
        elif instruction == 1:  # add
            return self.add(index, mode)
        elif instruction == 2:  # multiply
            return self.multiply(index, mode)
        elif instruction == 3:  # read and store
            return self.readAndStore(index, mode, args)
        elif instruction == 4:  # return value
            return self.returnVal(index, mode)

    def add(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        self.instructions[self.instructions[index + 3]] = arg1 + arg2
        return [index + 4]

    def multiply(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        self.instructions[self.instructions[index + 3]] = arg1 * arg2
        return [index + 4]

    def readAndStore(self, index, mode, args):
        self.instructions[self.instructions[index + 1]] = args[0]
        return [index + 2]

    def returnVal(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        return [index + 2, arg1]


with open("input.txt") as f:
    data = f.read()
instructions = list(map(int, data.split(",")))

iterpreter = Intcode(instructions)
index = 0
args = [1]
while index != -1:
    res = iterpreter.interpreter(index, args)
    index = res[0]
    if res.__len__() > 1:
        print(res[1])
