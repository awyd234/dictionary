# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from Word import Word


def main():
    while True:
        input_word = input("Input Your Word: ")
        if input_word.strip() == "Exit":
            print("Thanks, bye ~")
            break
        elif input_word.strip() == "Clear":
            os.system("clear")
        else:
            new_word = Word(input_word.strip())
            new_word.process_word()


if __name__ == '__main__':
    main()
