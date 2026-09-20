from commands import NoopCmd, ExitCmd

from .base_screen import BaseScreen
from commands.tournament_list import TournamentListCmd

class TournamentView(BaseScreen):
    """Shows one tournament's details and an action menu."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        t = self.tournament
        print(f"=== {t.name} ===")
        print(f"Venue: {t.venue}")
        print(f"Dates: {t.start_date.strftime('%d-%m-%Y')} "
              f"to {t.end_date.strftime('%d-%m-%Y')}")
        print(f"Rounds: {t.number_of_rounds}")
        print(f"Current round: {t.current_round}")
        print(f"Completed: {t.completed}")
        print(f"Players registered: {len(t.players)}")

    def get_command(self):
        while True:
            print("\nType R to return to the main menu.")
            print("Type X to exit.")
            value = self.input_string()
            if value.upper() == "R":
                return TournamentListCmd()
            elif value.upper() == "X":
                return ExitCmd()