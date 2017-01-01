# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
import json
import os


def look_for_word(word):
    url = "https://api.shanbay.com/bdc/search/?word={}"
    result_unicode = requests.get(url.format(word)).text
    result_json = json.loads(result_unicode)

    if result_json['status_code'] == 1:
        print("\t", result_json['msg'])
    else:
        result_data = result_json['data']
        cn_definition = result_data['cn_definition']['defn']
        cn_definition_list = cn_definition.split('\n')
        for each in cn_definition_list:
            print("\t", each)


def main():
    word = ""
    while True:
        word = input("Input Your Word: ")
        if word == "Exit":
            print("Thanks, bye ~")
            break
        elif word == "Clear":
            os.system(str.lower(word))
        else:
            look_for_word(word)


if __name__ == '__main__':
    main()
