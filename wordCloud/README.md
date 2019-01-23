### 可以对excel,csv,txt等3种不同格式的文件中的词语进行词云生成，（以后有时间可以扩展成对多个文件的操作）
基于python<br/>
用到的库：matplotlib、jieba、wordcloud、scipy、pandas、numpy<br/>
安装方法：
pip install jieba<br/>
pip install wordcloud......

linux平台有字体问题，需要下载字体，在fonts目录下已经下载

##edit.prop,为配置文件：
```
1.分析词云的文件：
filename=<data.txt>
2.xls,csv等文件，要分析的那以列的表头名称，txt文件可忽略
title=<Country>
3.希望过滤的字词汇
ignoreword=<社会,保障局,和,）,（,中国,中心>
4.词云背景图片
background=<love.jpg>
5.词云字体
fontfile=<STFANGSO.TTF>
6.词云背景颜色
background_color=<white>
7.最多显示的词数量
max_words=<200>
8.词语出现的频率，低于多少不考虑显示
ignor_blow_num=<1>
9.图片宽
picture_width=<500>
10.图片高
picture_height=<300>
```
## 效果如下:
### 唐诗三百首txt
![image](https://raw.githubusercontent.com/425776024/quick_word_cloud/master/shi300.png)
### 2013届大学毕业生走向数据xls
![image](https://raw.githubusercontent.com/425776024/quick_word_cloud/master/show.png)
<br/>
