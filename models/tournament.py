import json
import random
from datetime import datetime

from models.match import Match
from models.round import Round


class Tournament:
    DATE_FORMAT = "%d-%m-%Y"

    def __init__(
        self,
        name,
        venue,
        start_date,
        end_date,
        number_of_rounds,
        players=None,
        rounds=None,
        current_round=1,
        completed=False,
    ):
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

    def create_first_round(self):
        """Random pairings for round one."""
        if len(self.players) % 2 != 0:
            raise ValueError("Odd number of players!")
        shuffled = self.players[:]
        random.shuffle(shuffled)
        return Round(matches=[Match(shuffled[i], shuffled[i + 1]) for i in range(0, len(shuffled), 2)])

    def get_points(self):
        points = {p: 0 for p in self.players}
        for rnd in self.rounds:
            for match in rnd.matches:
                if not match.completed:
                    continue
                if match.winner:
                    points[match.winner] += 1
                else:
                    points[match.player1] += 0.5
                    points[match.player2] += 0.5
        return points

    def create_next_round(self):
        """Creates the next round based on the current points."""
        if self.completed:
            raise ValueError("This tournament is already completed!")
        if self.current_round is None or self.current_round >= self.number_of_rounds:
            raise ValueError("All rounds have already been played!")
        points = self.get_points()
        sorted_players = sorted(self.players, key=lambda p: points[p], reverse=True)
        matches = []
        for i in range(0, len(sorted_players), 2):
            matches.append(Match(sorted_players[i], sorted_players[i + 1]))
        return Round(matches=matches)

    def save(self, filepath):
        with open(filepath, "w") as fp:
            json.dump(self.serialize(), fp, indent=4)

    @classmethod
    def load(cls, filepath):
        with open(filepath) as fp:
            return cls.deserialize(json.load(fp))


if __name__ == "__main__":
    print("--- completed.json ---")
    t = Tournament.load("data/tournaments/completed.json")
    print(t.name)
    print(len(t.players), "players,", len(t.rounds), "rounds")
    print(t.rounds[0].matches[0].winner)
    print(t.get_points())
    try:
        t.create_next_round()
    except ValueError as e:
        print("create_next_round:", e)

    print("--- in-progress.json ---")
    t2 = Tournament.load("data/tournaments/in-progress.json")
    print(t2.name)
    print(len(t2.players), "players,", len(t2.rounds), "rounds")
    print(t2.get_points())
    print("next round:", [m.serialize() for m in t2.create_next_round().matches])
