#!/usr/bin/env python
# coding=utf-8

from WCCreator import *

class TextWordCreator(WCCreator):
    def __init__(self,fn):
        WCCreator.__init__(self,fn)

    def get_frequent_words(self):
        comment_text = open(self.filename,'r',encoding='UTF-8').read()
        cut_text = " ".join(jieba.cut(comment_text))
        return cut_text
    def show(self,font_name='STFANGSO.TTF',bg='love.jpg',max_words=100,background_color="white",max_font_size=100, random_state=42,width=500, height=300, margin=2):
        # 读取一个txt文件
        text = open(self.filename, 'r',encoding='UTF-8').read()
        # 读入背景图片
        bg_pic = imread(bg)
        # 生成词云
        wordcloud = WordCloud(font_path="fonts/"+font_name, background_color=background_color,
                         max_words=max_words,
                         mask=bg_pic,
                         max_font_size=max_font_size, random_state=random_state, width=width, height=height, margin=margin).generate(text)
        word_cloud = wordcloud.generate(self.get_frequent_words())  # 产生词云
        image_colors = ImageColorGenerator(bg_pic)
        # 显示词云图片
        plt.axis('off')
        plt.imshow(wordcloud.recolor(color_func=image_colors))
        plt.show()
