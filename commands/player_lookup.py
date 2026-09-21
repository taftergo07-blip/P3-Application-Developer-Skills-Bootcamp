import os

from models.player import Player

CLUB_DIR = "data/clubs"


def all_players():
    """Returns a {chess_id: Player} dict of every player across all clubs."""
    lookup = {}
    for filename in os.listdir(CLUB_DIR):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(CLUB_DIR, filename)) as fp:
            import json
            data = json.load(fp)
        for p in data["players"]:
            player = Player(**p)
            lookup[player.chess_id] = player
    return lookup