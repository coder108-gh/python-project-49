#!usr/bin/env python3
from random import randint


def gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def get_tasks(task_count=3, low=1, up=35) -> list:
    tasks = []
    for _ in range(task_count):
        num1 = randint(low, up)
        num2 = randint(low, up)
        correct_ans = gcd(num1, num2)
        tasks.append((f'{num1} {num2}', correct_ans))
    return tasks
