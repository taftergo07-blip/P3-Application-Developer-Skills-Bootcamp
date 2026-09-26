from commands.enter_results import EnterResultsCmd
from commands.player_lookup import all_players
from .base_screen import BaseScreen


class EnterResults(BaseScreen):
    """Asks for the winner of each match in the current round."""

    def __init__(self, tournament):
        self.tournament = tournament

    def player_label(self, chess_id, players):
        player = players.get(chess_id)
        if player:
            return f"{player.name} ({chess_id})"
        return chess_id

    def display(self):
        t = self.tournament
        print(f"=== Enter results: Round {len(t.rounds)} ===")

    def get_command(self):
        t = self.tournament
        current_round = t.rounds[-1]
        results = []
        players = all_players()
        for match in current_round.matches:
            p1, p2 = match.player1, match.player2
            label1 = self.player_label(p1, players)
            label2 = self.player_label(p2, players)
            print(f"\n{label1} vs {label2}")
            print(f"  1 - {label1} wins")
            print(f"  2 - {label2} wins")
            print(f"  D - Draw")
            
            while True:
                choice = self.input_string().upper()
                if choice == "1":
                    results.append(p1)
                    break
                elif choice == "2":
                    results.append(p2)
                    break
                elif choice == "D":
                    results.append(None)  # None = draw
                    break
        return EnterResultsCmd(t, results)
