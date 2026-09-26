from commands import ExitCmd
from commands.tournament_list import TournamentListCmd
from commands.player_lookup import all_players

from .base_screen import BaseScreen


class TournamentReport(BaseScreen):
    """Displays the full tournament report: standings and all rounds."""

    def __init__(self, tournament):
        self.tournament = tournament

    def player_label(self, chess_id, players):
        player = players.get(chess_id)
        if player:
            return f"{player.name} ({chess_id})"
        return chess_id
    
    def display(self):
        players = all_players()
        t = self.tournament
        print(f"=== Report: {t.name} ===")
        print(f"Venue: {t.venue}")
        print(f"Dates: {t.start_date.strftime('%d-%m-%Y')} "
              f"to {t.end_date.strftime('%d-%m-%Y')}")

        print("\n--- Standings ---")
        points = t.get_points()
        ranked = sorted(points.items(), key=lambda pair: pair[1], reverse=True)
        for rank, (player, score) in enumerate(ranked, 1):
            print(f"{rank}. {self.player_label(player, players)} - {score} pts")

        print("\n--- Rounds ---")
        for i, rnd in enumerate(t.rounds, 1):
            print(f"\nRound {i}:")
            for match in rnd.matches:
                player1_label = self.player_label(match.player1, players)
                player2_label = self.player_label(match.player2, players)
                if match.completed:
                    result = match.winner if match.winner else "Draw"
                else:
                    result = "not played"
                print(f"  {player1_label} vs {player2_label} -> {result}")
    def get_command(self):
        print("\nType R to return to the main menu, X to exit.")
        while True:
            value = self.input_string().upper()
            if value == "R":
                return TournamentListCmd()
            elif value == "X":
                return ExitCmd()
