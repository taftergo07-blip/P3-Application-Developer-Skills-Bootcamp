import json
import os

from models.player import Player

lookup = {}

for filename in os.listdir("data/clubs"):
    with open("data/clubs/" + filename) as fp:
        data = json.load(fp)
    for p in data["players"]:
        player = Player(**p)
        lookup[player.chess_id] = player

chess_id = input("Enter a Chess ID: ")

if chess_id in lookup:
    player = lookup[chess_id]
    print(player.name)
    print(player.email)
    print(player.birthday)
else:
    print("Player not found.")