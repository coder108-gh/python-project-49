#!usr/bin/env python3
from ..engine import play_game
from ..games.brain_gcd import get_tasks


def main() -> None:
    GAME_TEXT = 'Find the greatest common divisor of given numbers.'
    tasks = get_tasks()
    play_game(GAME_TEXT, tasks)


if __name__ == "__main__":
    main()
