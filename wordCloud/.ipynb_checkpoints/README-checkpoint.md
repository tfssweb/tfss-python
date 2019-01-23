### 1-------分析了黑龙江科技大学2013界毕业生走向

用到的库：matplotlib、jieba、wordcloud、scipy
安装方法：
pip install jieba
pip install wordcloud

linux平台有字体问题，需要下载字体，在fonts目录下已经下载
```
## 结巴分词


#读入背景图片

# //根据词频生成词云
my_wordcloud =wc1.generate_from_frequencies(pos_text)
#背景图片
image_colors = ImageColorGenerator(back_coloring)
#图片尺寸
plt.figure(figsize=(60,20)) 
plt.axis("off")
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.show()

```
## 最后结果:
![image](https://github.com/425776024/usthDataAnals/blob/master/show.png?raw=true)
<br/>
