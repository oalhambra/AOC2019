import queue
import threading


class Intcode:

    def __init__(self, instructions, inputBuffer, outputBuffer=queue.Queue()):
        self.instructions = instructions
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer

    def interpreter(self, index):
        instruction = self.instructions[index] % 100
        mode = int(self.instructions[index] / 100)

        if instruction == 99:
            return -1
        elif instruction == 1:  # add
            return self.add(index, mode)
        elif instruction == 2:  # multiply
            return self.multiply(index, mode)
        elif instruction == 3:  # read and store
            return self.readAndStore(index, mode)
        elif instruction == 4:  # return value
            return self.returnVal(index, mode)
        elif instruction == 5:  # jump-if-true
            return self.jumpIfTrue(index, mode)
        elif instruction == 6:  # jump-if-false
            return self.jumpIfFalse(index, mode)
        elif instruction == 7:  # less than
            return self.lesThan(index, mode)
        elif instruction == 8:  # equals
            return self.equals(index, mode)

    def start(self):
        t = threading.Thread(target=self.runProgram, args=())
        t.start()
        return t

    def runProgram(self):
        index = 0
        while index != -1:
            index = self.interpreter(index)

    # instructions code
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
        return index + 4

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
        return index + 4

    def readAndStore(self, index, mode):
        self.instructions[self.instructions[index + 1]] = self.inputBuffer.get(True)
        return index + 2

    def returnVal(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        self.outputBuffer.put(arg1)
        return index + 2

    def jumpIfTrue(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        if arg1 != 0:
            return arg2
        else:
            return index + 3

    def jumpIfFalse(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        if arg1 == 0:
            return arg2
        else:
            return index + 3

    def lesThan(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]

        if arg1 < arg2:
            res = 1
        else:
            res = 0
        self.instructions[self.instructions[index + 3]] = res
        return index + 4

    def equals(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]

        if arg1 == arg2:
            res = 1
        else:
            res = 0
        self.instructions[self.instructions[index + 3]] = res
        return index + 4


import itertools

with open("input.txt") as f:
    data = f.read()
instructions = list(map(int, data.split(",")))

allOptions = list(itertools.permutations([5, 6, 7, 8, 9]))

results = []
for option in allOptions:
    inputA = queue.Queue()
    inputA.put(option[0])
    inputB = queue.Queue()
    inputB.put(option[1])
    inputC = queue.Queue()
    inputC.put(option[2])
    inputD = queue.Queue()
    inputD.put(option[3])
    inputE = queue.Queue()
    inputE.put(option[4])

    inputA.put(0)
    amplifierA = Intcode(instructions.copy(), inputA, inputB)
    tA = amplifierA.start()
    amplifierB = Intcode(instructions.copy(), inputB, inputC)
    tB = amplifierB.start()
    amplifierC = Intcode(instructions.copy(), inputC, inputD)
    tC = amplifierC.start()
    amplifierD = Intcode(instructions.copy(), inputD, inputE)
    tD = amplifierD.start()
    amplifierE = Intcode(instructions.copy(), inputE, inputA)
    tE = amplifierE.start()

    tE.join()
    results.append(amplifierE.outputBuffer.get())

print(max(results))
