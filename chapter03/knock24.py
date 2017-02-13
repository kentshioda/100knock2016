#!/usr/bin/python
#_*_coding:utf-8_*_

from knock20 import get_UK_text
import re


def main():
    char_1 = re.compile(r"ファイル:(?P<name>.*?)\|")
    for line in get_UK_text().split("\n"):
        #print type(line)

        match_obj = char_1.search(line)
        if match_obj:
            print line
            print match_obj.group("name")


def miyazaki():
    re_file = re.compile('ファイル:(?P<name>.+?)\|')
    for line in get_UK_text().split('\n'):
        match = re_file.search(line)
        if match is not None:
            print(match.group('name'))


if __name__ == '__main__':
    #main()
    miyazaki()
