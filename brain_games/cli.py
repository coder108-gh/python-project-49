#!/usr/bin/env python3
import prompt


def get_username() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    return name


def greeting_user(name: str) -> None:
    print(f'Hello, {name}!')


def welcome_user() -> None:
    name = get_username()
    greeting_user(name)


def play_round(question, correct_ans) -> bool:
    print(f'Question: {question}')
    PROMPT_TEXT = 'Your answer: '
    ans = None
    if type(correct_ans) is str:
        ans = prompt.string(PROMPT_TEXT)
    if type(correct_ans) is int:
        ans = prompt.integer(PROMPT_TEXT)
    if ans != correct_ans:
        print(
            f"'{ans}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
        return False
    print('Correct!')
    return True


def play_game(game_text: str, tasks: list) -> None:
    name = get_username()
    greeting_user(name)
    print(game_text)
    for question, correct_ans in tasks:
        if not play_round(question, correct_ans):
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
