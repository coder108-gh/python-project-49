#!usr/bin/env python3
from random import randint
from .brain_common import play_game


def is_prime(num):
    dv = 2
    while num % dv != 0:
        dv += 1
    return dv == num


def get_tasks(task_count=3, low=1, up=100) -> list:
    tasks = []
    for _ in range(task_count):
        num = randint(low, up)
        correct_ans = 'no'
        if is_prime(num):
            correct_ans = 'yes'
        tasks.append((num, correct_ans))
    return tasks


def main() -> None:
    GAME_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    tasks = get_tasks()
    play_game(GAME_TEXT, tasks)


if __name__ == "__main__":
    main()
