#!/usr/bin/python
#_*_coding:utf-8_*_

from knock30 import make_mecab_list


def main():
    for sentence_list in make_mecab_list():
        combination3 = zip(*[sentence_list[i:] for i in range(3)])
        for combs in combination3:
            if combs[0]["pos"] == "名詞" and combs[1]["surface"] == "の" and combs[2]["pos"] == "名詞":
                print str(combs[0]["surface"]) + str(combs[1]["surface"]) + str(combs[2]["surface"])

if __name__ == '__main__':
    main()
