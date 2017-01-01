# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
import json
import os


URL = "https://api.shanbay.com"
SEARCH_PATH = "/bdc/search/?word={}"


STATUS_CODE_CONSTANT = {
    "CANNOT FIND THE MEANING": 1,
    "Fail to parse the json": 1001
}


class Word:
    word = ""
    status_code = 0
    msg = ""
    cn_definition_list = []

    def __init__(self, input_word):
        self.word = input_word

    def process_word(self):
        self.look_for_word()
        self.display_result()

    def look_for_word(self):
        url_path = URL + SEARCH_PATH.format(self.word)
        result_unicode = requests.get(url_path.format(self.word)).text
        try:
            result_json = json.loads(result_unicode)
            self.status_code = result_json['status_code']

            if self.status_code == STATUS_CODE_CONSTANT["CANNOT FIND THE MEANING"]:
                self.msg = result_json['msg']
                return
            else:
                result_data = result_json['data']
                cn_definition = result_data['cn_definition']['defn']
                self.cn_definition_list = cn_definition.split('\n')

        except Exception as ex:
            self.status_code = STATUS_CODE_CONSTANT["Fail to parse the json"]
            self.msg = "Fail to parse the json"
            print(ex)

    def display_result(self):
        if self.status_code != 0:
            print("\t", self.msg)
        else:
            for each in self.cn_definition_list:
                print("\t", each)


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
