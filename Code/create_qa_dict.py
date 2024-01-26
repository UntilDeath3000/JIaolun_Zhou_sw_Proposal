#!/usr/bin/env python
# coding=utf-8
"""
@author: Zonesion XB.Wei
@file: create_qa_dict.py
@time: 2019/4/9
@software: PyCharm
@Desc：中文分词并构建问答key-value数据集
"""

import json
import jieba
from tools import readjson, savejson

def readfile(file):
    """
    读取txt文件
    """
    with open(file, 'r', encoding='utf-8') as f:
        word_list = []
        for line in f.readlines():
            word_list.append(line.strip())
    return word_list

def movestopwords(sentence):
    """
    删除停用词
    """
    stopword = readfile('data/stopWord.txt')
    res = []
    for word in sentence:
        if word not in stopword:
            res.append(word)
    res = ' '.join(res)
    return res

if __name__ == '__main__':

    file = 'data/qa_dict.json'
    data = readjson(file)

    Q_list = data.keys()

    Q_dict = {}
    # create Q -> segmentation
    for i in Q_list:
        # jieba中文分词
        sentence = jieba.cut(i)
        # 去除停用词
        cut_sentence = movestopwords(sentence)
        Q_dict[i] = {'segmentation': cut_sentence}

    # print(Q_dict)
    Q_file = 'data/Q_dict.json'
    savejson(Q_file, Q_dict)
    print("问题数据集保存完成")

    A_dict = {}
    # Create q&a key-value pairs
    for k, v in data.items():
        for k1, v1 in v.items():
            A_dict[k] = v[k1]
    # print(A_dict)

    A_file = 'data/A_dict.json'
    savejson(A_file, A_dict)
    print("答案数据集保存完成")
