import jieba
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

with open('revue.txt', 'r', encoding="UTF-8") as file1:
    content = "".join(file1.readlines())
content_after = "".join(jieba.cut(content, cut_all=True))
##添加的代码,把刚刚你保存好的图片用Image方法打开,
##然后用numpy转换了一下
images = Image.open("aijo.jpg")
maskImages = np.array(images)

##修改了一下wordCloud参数,就是把这些数据整理成一个形状,
##具体的形状会适应你的图片的.
wc = WordCloud(font_path="/Users/vodka/Downloads/msyhl.ttc", background_color="white", max_words=5000, max_font_size=200, width=2500,
               height=1500, mask=maskImages).generate(content)
plt.imshow(wc)

wc.to_file('star.png')