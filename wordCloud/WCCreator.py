import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
from wordcloud import *
from collections import defaultdict
from scipy.misc import imread
import re
class WCCreator:
    #词云文件，当前只有一个，以后扩展多个？
    filename = ''
    ignore_word_list=[]
    ignor_blow_num=5
    def __init__(self,fn,ignwl=[],ignor_blow_num=3):
        self.filename=fn
        self.ignore_word_list=ignwl
        self.ignor_blow_num=ignor_blow_num
    '''
       显示词云图片
       max_words=200,词云显示的最大词数
       mask=back_coloring,设置背景图片
        max_font_size=100, random_state=42,width=500, height=300, margin=2
    '''
    def show(self,frequentWord={},font_name='STFANGSO.TTF',bg='love.jpg',max_words=100,background_color="white",max_font_size=100, random_state=42,width=500, height=300, margin=2):
        back_coloring = imread(bg)
        wc1d = WordCloud(font_path="fonts/"+font_name, background_color=background_color,
                         max_words=max_words,  # 词云显示的最大词数
                         mask=back_coloring,  # 设置背景图片
                         max_font_size=max_font_size, random_state=random_state, width=width, height=height, margin=margin)
        my_wordcloud = wc1d.generate_from_frequencies(frequentWord)
        # 背景图片
        image_colors = ImageColorGenerator(back_coloring)
        # 图片尺寸
        # plt.figure(figsize=(50, 30))
        plt.axis("off")
        plt.imshow(my_wordcloud.recolor(color_func=image_colors))
        plt.show()

    def jieba_words(self,dataItems):
        dat_fc = []
        data_test = list(dataItems)
        for i in data_test:
            ct_w = jieba.cut(i)
            ct_l = list(ct_w)
            dat_fc.append(ct_l)

        frequentWord = defaultdict(int)
        for i in dat_fc:
            for j in i:
                if (j not in self.ignore_word_list):
                    frequentWord[j] += i.count(j)
        keys = list(frequentWord.keys())
        for k in keys:
            if frequentWord[k] < self.ignor_blow_num:
                frequentWord.pop(k)
        return frequentWord