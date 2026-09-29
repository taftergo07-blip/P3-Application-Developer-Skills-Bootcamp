import os

from models.tournament import Tournament

from .base import BaseCommand
from .context import Context

TOURNAMENT_DIR = "data/tournaments"


class TournamentListCmd(BaseCommand):
    """Loads every tournament from disk and opens the main menu."""

    def __init__(self, force_list=False):
        self.force_list = force_list

    def execute(self):
        tournaments = []
        for filename in os.listdir(TOURNAMENT_DIR):
            if not filename.endswith(".json"):
                continue
            filepath = os.path.join(TOURNAMENT_DIR, filename)
            tournament = Tournament.load(filepath)
            tournament.filepath = filepath
            tournaments.append(tournament)

        tournaments.sort(key=lambda t: t.start_date, reverse=True)

        in_progress = [t for t in tournaments if not t.completed]
        if not self.force_list and len(in_progress) == 1:
            return Context("tournament-view", tournament=in_progress[0])

        return Context("main-menu", tournaments=tournaments)