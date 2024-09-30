#!/usr/bin/env python3
import prompt

def welcome_user()->None:
    name = prompt.string('May I have your name ? ')
    print('Welcome to the Brain Games!')
    print(f'Hello, {name}!')
