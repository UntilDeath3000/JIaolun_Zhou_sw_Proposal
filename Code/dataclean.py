#!/usr/bin/env python
#coding=utf-8
"""
@author: Zonesion XB.Wei
@file: dataclean.py
@time: 2019/4/9
@software: PyCharm
@Desc：data process
"""
from tools import readjson, savejson
# 测试数据集
file = 'WebQA.v1.0/me_test.ann.json'
data = readjson(file)
# 问答词典
qa_dict = {}
for k, v in data.items():
    keys = data[k]['question']
    qa_dict[keys] = data[k]['evidences']
# 保存问答词典
savefile = 'data/qa_dict.json'
savejson(savefile, qa_dict)
