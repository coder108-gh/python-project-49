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
