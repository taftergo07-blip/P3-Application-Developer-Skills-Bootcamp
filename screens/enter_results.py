from commands.enter_results import EnterResultsCmd

from .base_screen import BaseScreen


class EnterResults(BaseScreen):
    """Asks for the winner of each match in the current round."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        t = self.tournament
        print(f"=== Enter results: Round {len(t.rounds)} ===")

    def get_command(self):
        t = self.tournament
        current_round = t.rounds[-1]
        results = []
        for match in current_round.matches:
            p1, p2 = match.player1, match.player2
            print(f"\n{p1} vs {p2}")
            print(f"  1 - {p1} wins")
            print(f"  2 - {p2} wins")
            print("  D - Draw")
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
