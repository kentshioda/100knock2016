#!/usr/bin/python
#_*_coding:utf-8_*_

from knock30 import make_mecab_list
from collections import defaultdict


def main():
    word2count = defaultdict(lambda: int())
    for sentence_list in make_mecab_list():
        for word in sentence_list:
            word2count[word["surface"]] += 1
    for word, count in sorted(word2count.items(), key=lambda x: -x[1]):
        print str(word) + "\t" + str(count)


if __name__ == '__main__':
    main()
