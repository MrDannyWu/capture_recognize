#!/usr/bin/env python
# coding=utf-8
import os
from collections import Counter

file_list = os.listdir('../sample/train')
file_name_list = []
for i in file_list:
    file_name_list.append(i.split('_')[0])
print(file_name_list)

file_name_dict = dict(Counter(file_name_list))
print(file_name_dict)
for key, value in file_name_dict.items():
    if value == 2:
        print(key, value)

