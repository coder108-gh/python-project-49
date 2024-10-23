#!usr/bin/env python3
from ..engine import play_game
from ..games.brain_prime import get_tasks


def main() -> None:
    GAME_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    tasks = get_tasks()
    play_game(GAME_TEXT, tasks)


if __name__ == "__main__":
    main()
