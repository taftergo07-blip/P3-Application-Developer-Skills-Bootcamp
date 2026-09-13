class Match:
    def __init__(self, player1, player2, completed=False, winner=None):
        self.player1 = player1
        self.player2 = player2
        self.completed = completed
        self.winner = winner

    def serialize(self):
        return {
            "players": [self.player1, self.player2],
            "completed": self.completed,
            "winner": self.winner,
        }

    @classmethod
    def deserialize(cls, data):
        return cls(
            player1=data["players"][0],
            player2=data["players"][1],
            completed=data["completed"],
            winner=data["winner"],
        )
m = Match("AB12345", "CD67890")
d = m.serialize()
m2 = Match.deserialize(d)
print(m2.player1, m2.winner)

