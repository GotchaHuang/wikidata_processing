# Created by Gotcha on 2017/10/14.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os

pattern = re.compile('(.*) done')
useless_file = open('./repeat.txt')
useless_list = useless_file.read()
useless = pattern.findall(useless_list)


for _,__, files in os.walk('./MBA_经济百科'):
    for file in files:
        dot_index = file.rfind('.')
        slash_index = file.rfind('/')
        filename = file[slash_index+1:dot_index]
        if filename in useless:
            pos = './MBA_经济百科/' + file
            os.remove(pos)
            print(file + ' remove')
