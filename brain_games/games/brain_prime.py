#!usr/bin/env python3
from random import randint


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
