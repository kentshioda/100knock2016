#!/usr/bin/python
#_*_coding:utf-8_*_

from collections import defaultdict


def make_mecab_list():
    fin = open("neko.txt.mecab")
    d = defaultdict(lambda: 0)
    sentence_list = []
    all_list = []
    for line in fin:
        line = line.replace("\t", ",")
        line = line.strip().split(",")
        if line[0] == "EOS":
            all_list.append(sentence_list)
            sentence_list = []
            continue
        else:
            d["surface"] = line[0]
            d["base"] = line[7]
            d["pos"] = line[1]
            d["pos1"] = line[2]
            sentence_list.append(d)
            d = defaultdict(lambda: 0)
    return all_list


if __name__ == '__main__':
    all_list = make_mecab_list()
