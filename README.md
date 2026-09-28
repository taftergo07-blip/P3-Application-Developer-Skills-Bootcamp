# Chess Tournament Manager

A console application for running chess tournaments offline. Clubs can
manage tournaments from start to finish — registering players, recording
match results, generating pairings for each round, and viewing reports —
with all data stored locally in JSON files (no internet required).

## Features

- List all tournaments and open one to manage it
- View a tournament's details (venue, dates, rounds, registered players)
- Register players by searching club data by name or Chess ID
- Enter match results (win, loss, or draw) for the current round
- Automatically generate pairings for each new round based on standings
- View a full report: standings sorted by points, and every round's matches
- Save all changes to JSON immediately, so no data is lost

## Project structure

- **models/** — the data classes: `Player`, `Club`, `ClubManager` (provided),
  plus `Tournament`, `Round`, and `Match` (added for this project). Each model
  knows how to serialize itself to and from JSON.
- **screens/** — classes that display information and collect user input.
  Each screen returns a Command.
- **commands/** — classes that perform operations (following the template
  pattern via an `execute` method) and return the next Context.

## Installation
```
git clone https://github.com/taftergo07-blip/P3-Application-Developer-Skills-Bootcamp.git
cd P3-Application-Developer-Skills-Bootcamp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the application from the project root:
```
python main.py
```

Follow the on-screen menus: pick a tournament by number or create a new one,
then use the letter options (S to start, E to enter results, N to advance a
round, A to add a player, P to view the report).

## Code quality

The code follows PEP 8 and is checked with flake8 (max line length 119).
To regenerate the HTML lint report:
```
flake8 --format=html --htmldir=flake8_report
```
