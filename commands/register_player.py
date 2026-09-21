from .base import BaseCommand
from .context import Context


class RegisterPlayerCmd(BaseCommand):
    """Adds a player's chess ID to the tournament and saves."""

    def __init__(self, tournament, chess_id):
        self.tournament = tournament
        self.chess_id = chess_id

    def execute(self):
        t = self.tournament
        if self.chess_id not in t.players:
            t.players.append(self.chess_id)
            t.save(t.filepath)
        return Context("tournament-view", tournament=t)