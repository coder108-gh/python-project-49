#!usr/bin/env python3
from random import randint
from .brain_common import play_game


def get_rnd_num(att_cnt=3, low=1, up=100) -> list:
    numbers = []
    for _ in range(att_cnt):
        numbers.append(randint(low, up))
    return numbers


def get_tasks(task_count=3, low=1, up=100) -> list:
    tasks = []
    for _ in range(task_count):
        num = randint(low, up)
        correct_ans = 'yes'
        if num % 2 != 0:
            correct_ans = 'no'
        tasks.append((num, correct_ans))
    return tasks


def main() -> None:
    GAME_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
    tasks = get_tasks()
    play_game(GAME_TEXT, tasks)


if __name__ == "__main__":
    main()
