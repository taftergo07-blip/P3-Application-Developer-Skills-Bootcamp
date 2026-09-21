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
        t = self.tournament
        while True:
            print("\nActions:")
            if not t.completed:
                if t.rounds:
                    print("  E - Enter results for the current round")
                    print("  N - Advance to the next round")
                else:
                    print("  S - Start the tournament (first round)")
                print("  A - Add a player")
            print("  P - View report (players and points)")
            print("  R - Return to main menu")
            print("  X - Exit")

            value = self.input_string().upper()
            if value == "R":
                return TournamentListCmd()
            elif value == "X":
                return ExitCmd()
            elif value == "E" and not t.completed and t.rounds:
                from commands.noop import NoopCmd
                return NoopCmd("enter-results", tournament=t)
            elif value == "S" and not t.completed and not t.rounds:
                from commands.advance_round import AdvanceRoundCmd
                return AdvanceRoundCmd(t)
            elif value == "N" and not t.completed and t.rounds:
                confirm = self.input_string("Advance to the next round? (y/n)")
                if confirm.lower() == "y":
                    from commands.advance_round import AdvanceRoundCmd
                    return AdvanceRoundCmd(t)
            elif value == "P":
                from commands.noop import NoopCmd
                return NoopCmd("tournament-report", tournament=t)