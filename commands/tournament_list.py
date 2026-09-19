import os

from models.tournament import Tournament

from .base import BaseCommand
from .context import Context

TOURNAMENT_DIR = "data/tournaments"


class TournamentListCmd(BaseCommand):
    """Loads every tournament from disk and opens the main menu."""

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
        return Context("main-menu", tournaments=tournaments)