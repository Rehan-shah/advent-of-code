# mockData ="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lists = None

with open("input.txt", "r") as file:
    lists = file.readlines()


head = lists[0]


# blue_preset = 14
# red_preset = 12
# green_preset = 13


color_preset = {
    "blue": 14,
    "red": 12,
    "green": 13,
}

sum_game = 0


def check_if_follows_rule(color, ball_color):
    if color in ball_color:
        if int(ball_color.replace(color, "")) > color_preset[color]:
            return False
    return True


for list in lists:
    game_no = int(list[: list.index(":")].replace("Game", "").strip())
    games = list[list.index(":") + 1 :].strip().split(";")
    print(game_no)
    doesGameFollowRule = True
    for game in games:
        for ball_color in game.split(","):
            for color in ["blue", "green", "red"]:
                if check_if_follows_rule(color=color, ball_color=ball_color):
                    pass
                else:
                    doesGameFollowRule = False
    if doesGameFollowRule:
        sum_game += game_no


print("The answer ", sum_game)
