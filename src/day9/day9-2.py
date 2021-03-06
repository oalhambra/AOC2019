import queue
import threading


class Intcode:

    def __init__(self, instructions, inputBuffer=queue.Queue(), outputBuffer=queue.Queue()):
        self.instructions = instructions
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer
        self.relativeBase = 0
        self.instructions.extend([-1 for i in range(2 ** 20 - self.instructions.__len__())])

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
        elif instruction == 9:  # adjust relative base
            return self.adjustRelativeBase(index, mode)

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
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        elif mode % 10 == 2:
            arg2 = self.instructions[self.instructions[index + 2] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            self.instructions[self.instructions[index + 3]] = arg1 + arg2
        elif mode % 10 == 2:
            self.instructions[self.instructions[index + 3] + self.relativeBase] = arg1 + arg2
        return index + 4

    def multiply(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        elif mode % 10 == 2:
            arg2 = self.instructions[self.instructions[index + 2] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            self.instructions[self.instructions[index + 3]] = arg1 * arg2
        elif mode % 10 == 2:
            self.instructions[self.instructions[index + 3] + self.relativeBase] = arg1 * arg2
        return index + 4

    def readAndStore(self, index, mode):
        if mode % 10 == 0:
            self.instructions[self.instructions[index + 1]] = self.inputBuffer.get(True)
        elif mode % 10 == 2:
            self.instructions[self.instructions[index + 1] + self.relativeBase] = self.inputBuffer.get(True)
        return index + 2

    def returnVal(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        self.outputBuffer.put(arg1)
        return index + 2

    def jumpIfTrue(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        elif mode % 10 == 2:
            arg2 = self.instructions[self.instructions[index + 2] + self.relativeBase]
        if arg1 != 0:
            return arg2
        else:
            return index + 3

    def jumpIfFalse(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        elif mode % 10 == 2:
            arg2 = self.instructions[self.instructions[index + 2] + self.relativeBase]
        if arg1 == 0:
            return arg2
        else:
            return index + 3

    def lesThan(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        elif mode % 10 == 2:
            arg2 = self.instructions[self.instructions[index + 2] + self.relativeBase]

        if arg1 < arg2:
            res = 1
        else:
            res = 0
        mode = int(mode / 10)
        if mode % 10 == 0:
            self.instructions[self.instructions[index + 3]] = res
        elif mode % 10 == 2:
            self.instructions[self.instructions[index + 3] + self.relativeBase] = res
        return index + 4

    def equals(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        mode = int(mode / 10)
        if mode % 10 == 0:
            arg2 = self.instructions[self.instructions[index + 2]]
        elif mode % 10 == 1:
            arg2 = self.instructions[index + 2]
        elif mode % 10 == 2:
            arg2 = self.instructions[self.instructions[index + 2] + self.relativeBase]

        if arg1 == arg2:
            res = 1
        else:
            res = 0
        mode = int(mode / 10)
        if mode % 10 == 0:
            self.instructions[self.instructions[index + 3]] = res
        elif mode % 10 == 2:
            self.instructions[self.instructions[index + 3] + self.relativeBase] = res
        return index + 4

    def adjustRelativeBase(self, index, mode):
        if mode % 10 == 0:
            arg1 = self.instructions[self.instructions[index + 1]]
        elif mode % 10 == 1:
            arg1 = self.instructions[index + 1]
        elif mode % 10 == 2:
            arg1 = self.instructions[self.instructions[index + 1] + self.relativeBase]
        self.relativeBase += arg1
        return index + 2


with open("input.txt") as f:
    data = f.read()
instructions = list(map(int, data.split(",")))
boost = Intcode(instructions)
boost.start()
boost.inputBuffer.put(2)
print(boost.outputBuffer.get())
