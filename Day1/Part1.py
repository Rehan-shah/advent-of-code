lines = []


with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0

print(lines)

for line in lines:
    digits = [dig for dig in line if dig.isdigit()]
    sum += int(digits[0] + digits[-1])

print(sum)
