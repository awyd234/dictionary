# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
import json
import os


URL = "https://api.shanbay.com"
SEARCH_PATH = "/bdc/search/?word={}"


class Word:
    word = ""
    cn_definition_list = []

    def __init__(self, input_word):
        self.word = input_word

    def process_word(self):
        self.look_for_word()
        self.display_meanings()

    def look_for_word(self):
        url_path = URL + SEARCH_PATH.format(self.word)
        result_unicode = requests.get(url_path.format(self.word)).text
        result_json = json.loads(result_unicode)

        if result_json['status_code'] == 1:
            print("\t", result_json['msg'])
        else:
            result_data = result_json['data']
            cn_definition = result_data['cn_definition']['defn']
            self.cn_definition_list = cn_definition.split('\n')

    def display_meanings(self):
        for each in self.cn_definition_list:
            print("\t", each)


def main():
    while True:
        input_word = input("Input Your Word: ")
        if input_word == "Exit":
            print("Thanks, bye ~")
            break
        elif input_word == "Clear":
            os.system("clear")
        else:
            new_word = Word(input_word)
            new_word.process_word()


if __name__ == '__main__':
    main()
