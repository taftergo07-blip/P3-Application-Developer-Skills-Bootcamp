from models.match import Match
class Round:
    def __init__(self, matches=None):
        self.matches = matches if matches is not None else []

    def serialize(self):
        return {"matches": [m.serialize() for m in self.matches]}

    @classmethod
    def deserialize(cls, data):
        return cls(matches=[Match.deserialize(d) for d in data["matches"]])
