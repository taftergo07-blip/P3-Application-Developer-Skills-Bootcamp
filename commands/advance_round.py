from .base import BaseCommand
from .context import Context


class AdvanceRoundCmd(BaseCommand):
    """Generates the next round's pairings, or the first round, and saves."""

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        t = self.tournament
        if t.rounds:
            new_round = t.create_next_round()
        else:
            new_round = t.create_first_round()
        t.rounds.append(new_round)

        if len(t.rounds) >= t.number_of_rounds:
            t.completed = True
            t.current_round = None
        else:
            t.current_round = len(t.rounds)

        t.save(t.filepath)
        return Context("tournament-view", tournament=t)
