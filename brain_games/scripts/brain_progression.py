#!usr/bin/env python3
from random import randint
from random import choice
from ..cli import play_game


def get_progression(min_len=5, max_len=10, min_start=1, max_start=20,
                    min_step=1, max_step=5):
    start_pos = randint(min_start, max_start)
    progr_len = randint(min_len, max_len)
    progr_step = randint(min_step, max_step)
    progr = []
    for idx in range(progr_len):
        progr.append(start_pos + progr_step * idx)
    return progr


def get_string_progress(progress: list) -> str:
    tmp = []
    for num in progress:
        tmp.append(str(num))
    return ' '.join(tmp)


def get_tasks(task_count=3, low=1, up=35) -> list:
    tasks = []
    for _ in range(task_count):
        progr = get_progression(min_start=low, max_start=up)
        correct_ans = choice(progr)
        idx = progr.index(correct_ans)
        progr[idx] = '..'
        progr_str = get_string_progress(progr)
        tasks.append((progr_str, correct_ans))
    return tasks


def main() -> None:
    GAME_TEXT = 'What number is missing in the progression?'
    tasks = get_tasks()
    play_game(GAME_TEXT, tasks)


if __name__ == "__main__":
    main()
