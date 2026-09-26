from commands import NoopCmd, ExitCmd
from .base_screen import BaseScreen


class TournamentMenu(BaseScreen):
    """Main menu: lists all tournaments and lets the user pick one."""

    def __init__(self, tournaments):
        self.tournaments = tournaments

    def display(self):
        print("=== Tournaments ===")
        for idx, tournament in enumerate(self.tournaments, 1):
            status = "completed" if tournament.completed else "in progress"
            print(f"{idx}. {tournament.name} ({status})")

    def get_command(self):
        while True:
            print("\nType a tournament number to open it.")
            print("Type C to create a new tournament.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                number = int(value)
                if number in range(1, len(self.tournaments) + 1):
                    return NoopCmd(
                        "tournament-view",
                        tournament=self.tournaments[number - 1],
                    )
            elif value.upper() == "C":
                return NoopCmd("create-tournament")
            elif value.upper() == "X":
                return ExitCmd()