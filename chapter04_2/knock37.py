#!/usr/bin/python
#_*_coding:utf-8_*_

from knock30 import make_mecab_list
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


def make_plot(word2count):
    x = []
    y = []
    for word, count in sorted(word2count.items(), key=lambda x: -x[1])[:10]:
        x.append(str(word))
        y.append(float(count))

    plt.bar(x, y, align="center")
    plt.show()


def main():
    word2count = defaultdict(lambda: int())
    for sentence_list in make_mecab_list():
        for word in sentence_list:
            word2count[word["surface"]] += 1
    return word2count


if __name__ == '__main__':
    word2count = main()
    make_plot(word2count)
