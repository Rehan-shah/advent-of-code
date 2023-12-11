lists = None


mockData = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


# Real Data
with open("input.txt", "r") as file:
    lists = file.readlines()

## Mock Data
# lists = mockData.split("\n")


sum_game = 0


def check_if_follows_rule(color, ball_color):
    if color in ball_color:
        if int(ball_color.replace(color, "")) > color_preset[color]:
            return False
    return True


for list in lists:
    color_preset = {
        "blue": 0,
        "red": 0,
        "green": 0,
    }
    game_no = int(list[: list.index(":")].replace("Game", "").strip())
    games = list[list.index(":") + 1 :].strip().split(";")
    print(game_no)
    for game in games:
        for ball_color in game.split(","):
            for color in ["blue", "green", "red"]:
                if color in ball_color:
                    number_of_balls = int(ball_color.replace(color, ""))
                    if number_of_balls > color_preset[color]:
                        color_preset[color] = number_of_balls
    res = 1
    for key in color_preset:
        res *= color_preset[key]
    sum_game += res


print("The answer ", sum_game)
