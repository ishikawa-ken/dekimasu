#!/usr/bin/env python
# -*- cording: utf-8 -*-

import Levenshtein as lev


# [parameter]---------->
Threshold = 0.6    # 認識結果の閾値
# <---------------------


question_list = ["bring me the cupnoodle from the desk",\
                 "get the greenstick from the cupboard and put it on the desk",\
                 "give the chipstar to me"]


class distance(object):
    def __init__(self):
        global question_list

        self.question = question_list

    def check(self, string):
        result_final = 1.0
        num = 0

        for question in self.question:
             result = lev.distance(string, question)/(max(len(string), len(question)) *1.00)
             #print(result)
             if result_final >= result:
                 result_final = result
                 num = self.question.index(question)+1


        if result_final <= Threshold:
            return num
        else:
            #self.speak("One more time please")
            return 0
