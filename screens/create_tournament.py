from datetime import datetime

from commands.create_tournament import CreateTournamentCmd

from .base_screen import BaseScreen


class CreateTournament(BaseScreen):
    """Collects details for a new tournament."""

    def display(self):
        print("=== Create a new tournament ===")

    def input_date(self, prompt):
        while True:
            value = self.input_string(prompt, empty=True)
            try:
                datetime.strptime(value, "%d-%m-%Y")
                return value
            except ValueError:
                print("Please enter a valid date as dd-mm-yyyy.")

    def get_command(self):
        name = self.input_string("Tournament name", empty=True)
        venue = self.input_string("Venue", empty=True)
        start_date = self.input_date("Start date (dd-mm-yyyy)")
        end_date = self.input_date("End date (dd-mm-yyyy)")

        while True:
            rounds = self.input_string("Number of rounds", empty=True)
            if rounds.isdigit() and int(rounds) > 0:
                number_of_rounds = int(rounds)
                break
            print("Please enter a positive number.")

        return CreateTournamentCmd(
            name, venue, start_date, end_date, number_of_rounds
        )