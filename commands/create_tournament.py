import os

from models.tournament import Tournament

from .base import BaseCommand
from .context import Context

TOURNAMENT_DIR = "data/tournaments"


class CreateTournamentCmd(BaseCommand):
    """Creates a new tournament, saves it to a new JSON file, and opens it."""

    def __init__(self, name, venue, start_date, end_date, number_of_rounds):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds

    def execute(self):
        tournament = Tournament(
            name=self.name,
            venue=self.venue,
            start_date=self.start_date,
            end_date=self.end_date,
            number_of_rounds=self.number_of_rounds,
        )
        filename = self.name.replace(" ", "_").lower() + ".json"
        filepath = os.path.join(TOURNAMENT_DIR, filename)
        tournament.filepath = filepath
        tournament.save(filepath)
        return Context("tournament-view", tournament=tournament)