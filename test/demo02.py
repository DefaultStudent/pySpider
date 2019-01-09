import requests
import json
from bs4 import BeautifulSoup

# 请求数据
url = 'https://www.bilibili.com/bangumi/media/md102892/?spm_id_from=666.10.b_62616e67756d695f64657461696c.1'
# headers里面大小写均可
headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0)Gecko/20100101 Firefox/52.0"}
data = requests.get(url, headers=headers)
# print(data.text)

# 解析数据
soup = BeautifulSoup(data.text, 'lxml')
print(soup.prettify())


