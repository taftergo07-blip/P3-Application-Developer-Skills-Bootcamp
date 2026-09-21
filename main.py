from commands.tournament_list import TournamentListCmd
from screens.tournament_menu import TournamentMenu
from screens.tournament_view import TournamentView
from screens.enter_results import EnterResults
from screens.tournament_report import TournamentReport
from screens.register_player import RegisterPlayer


class App:
    """The main controller for the tournament management program"""

    SCREENS = {
        "main-menu": TournamentMenu,
        "tournament-view": TournamentView,
        "enter-results": EnterResults,
        "exit": False,
        "tournament-report": TournamentReport,
        "register-player": RegisterPlayer,
    }

    def __init__(self):
        command = TournamentListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            screen = self.SCREENS[self.context.screen]
            try:
                command = screen(**self.context.kwargs).run()
                self.context = command()
            except KeyboardInterrupt:
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    App().run()
