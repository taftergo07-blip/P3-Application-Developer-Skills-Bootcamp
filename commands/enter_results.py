from models.tournament import Tournament

from .base import BaseCommand
from .context import Context


class EnterResultsCmd(BaseCommand):
    """Records winners for the current round's matches and saves."""

    def __init__(self, tournament, results):
        self.tournament = tournament
        self.results = results  # list of winner values, one per match

    def execute(self):
        t = self.tournament
        current_round = t.rounds[-1]
        for match, winner in zip(current_round.matches, self.results):
            match.winner = winner
            match.completed = True
        t.save(t.filepath)
        return Context("tournament-view", tournament=t)