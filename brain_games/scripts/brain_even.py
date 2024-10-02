#!usr/bin/env python3
from random import randint
import prompt
from ..cli import get_username
from ..cli import greeting_user


def get_rnd_num(att_cnt=3, low=1, up=100) -> list:
    numbers = []
    for _ in range(att_cnt):
        numbers.append(randint(low, up))
    return numbers


def is_correct_ans(num: int) -> bool:
    correct_ans = 'yes'
    if num % 2 != 0:
        correct_ans = 'no'

    print(f'Question: {num}')
    ans = prompt.string('Your answer: ')
    if ans == correct_ans:
        print('Correct!')
        return True
    print(f"'{ans}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
    return False


def main() -> None:
    name = get_username()
    greeting_user(name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    numbers = get_rnd_num()
    for num in numbers:
        if not is_correct_ans(num):
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
