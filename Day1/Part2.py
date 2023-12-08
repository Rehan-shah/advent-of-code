lines = []
units_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nieteen": 19,
}


mockData = """
two1nine
eightwothree
abcone2threexyz
eighthree
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
# # MockData testing lines
# lines = [line for line in mockData.split("\n") if line != ""]


# Real File rmeove
with open("input.txt", "r") as file:
    lines = file.readlines()
sum = 0
i = 0


def convertShit(line):
    found = True
    for key in units_dict:
        try:
            j = line.index(key)
            line = line[: j + 2] + str(units_dict[key]) + line[j + 2 :]
            found = False
            print(line)
        except:
            pass
    if found == False:
        return convertShit(line)
    return line

for line in lines:
    line = convertShit(line)
    digits = [c for c in line if c.isdigit()]

    if 3 >= i:
        print(line)
        i += 1
        print(digits)
    sum += int(digits[0] + digits[-1])

print("Total sum is:", sum)
#


# DIGITS_MAP = {
#     "oneight": "18",
#     "twone": "21",
#     "threeight": "38",
#     "fiveight": "58",
#     "sevenine": "79",
#     "eightwo": "82",
#     "eighthree": "83",
#     "nineight": "98",
#     "one": "1",
#     "two": "2",
#     "three": "3",
#     "four": "4",
#     "five": "5",
#     "six": "6",
#     "seven": "7",
#     "eight": "8",
#     "nine": "9",
# }
#
#
# def extract_digits(line: str) -> int:
#     for digit in DIGITS_MAP:
#         line = line.replace(digit, DIGITS_MAP[digit])
#     digits = [s for s in line if s.isnumeric()]
#     return int(digits[0] + digits[-1])
#
#
# INPUT = lines
#
#
# def main():
#     digits = [extract_digits(l) for l in INPUT.split()]
#     print(f"Sum is {sum(digits)}")
#
#
# if __name__ == "__main__":
#     main()
