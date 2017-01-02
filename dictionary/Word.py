# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
import json

from dictionary import config_parse


STATUS_CODE_CONSTANT = {
    "CANNOT FIND THE MEANING": 1,
    "Fail to parse the json": 1001
}


class Word:
    word = ""
    status_code = 0
    msg = ""
    cn_definition_list = []
    en_definition_dict = {}

    def __init__(self, input_word):
        self.word = input_word

    def process_word(self):
        self.look_for_word()
        self.display_result()

    def look_for_word(self):
        url_path = "{}/{}".format(config_parse.get_value("host", "shanbay_url"),
                                  config_parse.get_value("path", "shanbay_search_path"))
        param = {
            "word": self.word
        }
        request_result = requests.get(url_path, param)
        if request_result.status_code != 200:
            self.msg = "Fail to connect the api. Status code: {}".format(request_result.status_code)
            return
        else:
            result_unicode = request_result.text
        try:
            result_json = json.loads(result_unicode)
            self.status_code = result_json['status_code']

            if self.status_code == STATUS_CODE_CONSTANT["CANNOT FIND THE MEANING"]:
                self.msg = result_json['msg']
                return
            else:
                result_data = result_json['data']
                cn_definition = result_data['cn_definition']['defn']
                self.en_definition_dict = result_data['en_definitions']
                self.cn_definition_list = cn_definition.split('\n')

        except Exception as ex:
            self.status_code = STATUS_CODE_CONSTANT["Fail to parse the json"]
            self.msg = "Fail to parse the json"
            print(ex)

    def display_result(self):
        if self.status_code != 0:
            print("\t", self.msg)
        else:
            print("    英文意思：")
            for k, v in self.en_definition_dict.items():
                print("\t[{}]".format(k))
                for each in v:
                    print("\t    {}".format(each))
            print("    中文意思：")
            for each in self.cn_definition_list:
                print("\t", each)
