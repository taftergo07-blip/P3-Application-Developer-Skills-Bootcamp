from models.match import Match


class Round:
    def __init__(self, matches=None):
        self.matches = matches if matches is not None else []

    def serialize(self):
        return [m.serialize() for m in self.matches]

    @classmethod
    def deserialize(cls, data):
        return cls(matches=[Match.deserialize(d) for d in data])


"""m1 = Match("AB12345", "CD67890")
r = Round(matches=[m1])
print(r.serialize())
r2 = Round.deserialize(r.serialize())
print(r2.matches[0].player1)"""
