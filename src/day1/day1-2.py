with open("input.txt") as f:
    lines = f.readlines()
acc_fuel = 0
for line in lines:
    mass = int(line)
    while mass > 0:
        mass = int(mass / 3) - 2
        if mass > 0:
            acc_fuel += mass

print(acc_fuel)
