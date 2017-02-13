#!/usr/bin/python
#_*_coding:utf-8_*_

from knock30 import make_mecab_list


def main():
    for sentence_list in make_mecab_list():
        #print sentence_list
        for info_name2word_info in sentence_list:
            if info_name2word_info["pos"] == "動詞":
                print info_name2word_info["surface"]


if __name__ == '__main__':
    main()
