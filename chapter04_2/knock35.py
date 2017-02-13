#!/usr/bin/python
#_*_coding:utf-8_*_

from knock30 import make_mecab_list


def main():
    for sentence_list in make_mecab_list():
        nouns = []
        for word in sentence_list:
            if word["pos"] == "名詞":
                nouns.append(word["surface"])
            else:
                if len(nouns) > 1:
                    print "".join(nouns)
                nouns = []


if __name__ == '__main__':
    main()
