#!usr/bin/env python3
from ..engine import play_game
from ..games.brain_progression import get_tasks


def main() -> None:
    GAME_TEXT = 'What number is missing in the progression?'
    tasks = get_tasks()
    play_game(GAME_TEXT, tasks)


if __name__ == "__main__":
    main()
