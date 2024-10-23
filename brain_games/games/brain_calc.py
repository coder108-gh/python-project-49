#!usr/bin/env python3
from random import randint
from random import choice


def calc_result(op: str, num1: int, num2: int) -> int:
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    return 0


def get_tasks(task_count=3, low=1, up=35) -> list:
    OPERATIONS = ['+', '-', '*']
    tasks = []
    for _ in range(task_count):
        op = choice(OPERATIONS)
        num1 = randint(low, up)
        num2 = randint(low, up)
        correct_ans = calc_result(op, num1, num2)
        tasks.append((f'{num1} {op} {num2}', correct_ans))
    return tasks
