import requests
from bs4 import BeautifulSoup

# 请求数据
url = 'http://book.douban.com/latest'
# headers里面大小写均可
headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0)Gecko/20100101 Firefox/52.0"}
data = requests.get(url, headers=headers)
print(data.text)

# 解析数据
soup = BeautifulSoup(data.text, 'lxml')
print(soup)

# 观察到网页上的书按左右两边分布，按标签分别提取
books_left = soup.find('ul', {'class':'cover-col-4 clearfix'})
books_left = books_left.find_all('li')

books_right = soup.find('ul', {'class':'cover-col-4 pl20 clearfix'})
books_right = books_right.find_all('li')

books = list(books_left)+list(books_right)

# 对每一个图书区块进行相同的操作，获取图书信息
img_urls = []
titles = []
ratings = []
authors = []
details = []
for book in books:

    # 图书封面图片url地址
    img_url = book.find_all('a')[0].find('img').get('src')
    img_urls.append(img_url)
    # 图书标题
    title = book.find_all('a')[1].get_text()
    titles.append(title)
    # print(title)

    # 评价星级
    rating = book.find('p', {'class':'rating'}).get_text()
    rating = rating.replace('\n', '').replace(' ','')
    ratings.append(rating)

    # 作者及出版信息
    author = book.find('p', {'class':'color-gray'}).get_text()
    author = author.replace('\n', '').replace(' ', '')
    authors.append(author)

    # 图书简介
    detail = book.find_all('p')[2].get_text()
    detail = detail.replace('\n', '').replace(' ', '')
    details.append(detail)

print("img_urls: ", img_urls)
print("titles: ", titles)
print("ratings: ", ratings)
print("authors: ", authors)
print("details", details)