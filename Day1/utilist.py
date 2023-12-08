

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
two1twonine
eightwothree
abcone2threexyz
eighthree
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

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

print( "ans : ",convertShit(mockData.split("\n")[1]))

