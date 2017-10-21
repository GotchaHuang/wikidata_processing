# Created by Gotcha on 2017/10/13.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


for _, __, files in os.walk('./MBA_管理百科指定子类'):
    for file_name in files:
        old_name = './MBA_管理百科指定子类/' + file_name
        index = file_name.find('.')
        new_name = './MBA_管理百科指定子类/' + file_name[:index] + '.html'
        os.rename(old_name, new_name)
        print(file_name + 'done')
