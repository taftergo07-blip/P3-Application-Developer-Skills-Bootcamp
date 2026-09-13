import json
from datetime import datetime

from models.round import Round


class Tournament:
    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, name, venue, start_date, end_date, number_of_rounds,
                 players=None, rounds=None, current_round=1, completed=False):
        if not name:
            raise ValueError("Tournament name is required!")
        self.name = name
        self.venue = venue
        self.start_date = datetime.strptime(start_date, self.DATE_FORMAT)
        self.end_date = datetime.strptime(end_date, self.DATE_FORMAT)
        self.number_of_rounds = number_of_rounds
        self.players = players if players is not None else []
        self.rounds = rounds if rounds is not None else []
        self.current_round = current_round
        self.completed = completed

    def serialize(self):
        return {
            "name": self.name,
            "dates": {
                "from": self.start_date.strftime(self.DATE_FORMAT),
                "to": self.end_date.strftime(self.DATE_FORMAT),
            },
            "venue": self.venue,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "completed": self.completed,
            "players": self.players,
            "rounds": [r.serialize() for r in self.rounds],
        }

    @classmethod
    def deserialize(cls, data):
        return cls(
            name=data["name"],
            venue=data["venue"],
            start_date=data["dates"]["from"],
            end_date=data["dates"]["to"],
            number_of_rounds=data["number_of_rounds"],
            players=data["players"],
            rounds=[Round.deserialize(r) for r in data["rounds"]],
            current_round=data["current_round"],
            completed=data["completed"],
        )
if __name__ == "__main__":
    with open("data/tournaments/completed.json") as fp:
        t = Tournament.deserialize(json.load(fp))
    print(t.name)
    print(len(t.players), "players,", len(t.rounds), "rounds")
    print(t.rounds[0].matches[0].winner)    