#!/usr/bin/env python
# coding=utf-8

import re
from ExcelWordCreator import *
from CSVWordCreator import *
from TextWordCreator import *


def main():
    # with open('edit.prop', 'r', encoding='UTF-8') as f:
    #     for line in f.readlines():
    #         print(line)


    propFile = open('edit.prop','r',encoding='UTF-8')
    texts = propFile.read()
    print(texts)
    dicts = {}
    pattam='filename=<(.*)>[.\n]title=<(.*)>[.\n]ignoreword=<(.*)>[.\n]background=<(.*)>[.\n]fontfile=<(.*)>[.\n]background_color=<(.*)>[.\n]max_words=<(.*)>[.\n]ignor_blow_num=<(.*)>[.\n]picture_width=<(.*)>[.\n]picture_height=<(.*)>'
    matchFilename = re.match(pattam, texts, re.M | re.DOTALL)
    if matchFilename:
        dicts = {'fn': matchFilename.group(1), 'tt': matchFilename.group(2), 'ignw': matchFilename.group(3),
                 'bg': matchFilename.group(4),'ftf': matchFilename.group(5),'bccl': matchFilename.group(6),
                 'maxwords': matchFilename.group(7), 'ignorbelownum': matchFilename.group(8),
                 'picw': matchFilename.group(9),'pich': matchFilename.group(10)}
    else:
        print("No matchFilename!!")

    filename = dicts['fn']
    ignw = dicts['ignw']
    tt = dicts['tt']
    bg = dicts['bg']
    file_type = filename.split('.')[1]
    ignore_word_list = ignw.split(',')
    # ---------------------------------------------------------
    ftf = dicts['ftf']
    bccl = dicts['bccl']
    maxwords = dicts['maxwords']
    ignorbelownum = dicts['ignorbelownum']
    picw=dicts['picw']
    pich=dicts['pich']
    if file_type=='xls':
        excelWordCreator=ExcelWordCreator(filename,ignore_word_list,tt,int(ignorbelownum))
        frequentWord=excelWordCreator.get_frequent_words()
        excelWordCreator.show(frequentWord=frequentWord,font_name=ftf,bg=bg,background_color=bccl,max_words=int(maxwords),width=int(picw),height=int(pich))
    elif file_type=='csv':
        csvWordCreator = CSVWordCreator(filename, ignore_word_list, tt, int(ignorbelownum))
        frequentWord = csvWordCreator.get_frequent_words()
        csvWordCreator.show(frequentWord=frequentWord, font_name=ftf, bg=bg, background_color=bccl,max_words=int(maxwords), width=int(picw), height=int(pich))
    elif file_type=='txt':
        textCreator=TextWordCreator(filename)
        textCreator.show()

if __name__ == '__main__':
  main()