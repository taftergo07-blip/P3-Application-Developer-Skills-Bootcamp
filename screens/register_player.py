from commands.register_player import RegisterPlayerCmd
from commands.player_lookup import all_players

from .base_screen import BaseScreen


class RegisterPlayer(BaseScreen):
    """Search the club players and register one to the tournament."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("=== Register a player ===")

    def get_command(self):
        players = all_players()
        term = self.input_string("Search by name or chess ID")
        term = term.lower()

        matches = [
            p for p in players.values()
            if term in p.name.lower() or term in p.chess_id.lower()
        ]

        if not matches:
            print("No players found.")
            return RegisterPlayerCmd(self.tournament, None)

        for idx, p in enumerate(matches, 1):
            print(f"{idx}. {p.name} ({p.chess_id})")

        while True:
            choice = self.input_string("Pick a number")
            if choice.isdigit() and int(choice) in range(1, len(matches) + 1):
                chosen = matches[int(choice) - 1]
                return RegisterPlayerCmd(self.tournament, chosen.chess_id)