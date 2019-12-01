with open("input.txt") as f:
    lines = f.readlines()
acc_fuel = 0
for line in lines:
    fuel = int(int(line) / 3) - 2
    acc_fuel += fuel

print(acc_fuel)
