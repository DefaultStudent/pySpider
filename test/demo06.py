import requests
import xlsxwriter
import os
from bs4 import BeautifulSoup

if 'Myxlsxdata' not in os.listdir():
    os.mkdir('Myxlsxdata')
os.chdir('Myxlsxdata')

# 创建Excel表格
workbook = xlsxwriter.Workbook('movierank.xlsx')

# 设置表名
worksheet = workbook.add_worksheet('B站排行榜')

# 请求数据
url = 'https://www.bilibili.com/ranking/all/181/1/3'
# headers里面大小写均可
headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0)Gecko/20100101 Firefox/52.0"}
data = requests.get(url, headers=headers)
# print(data.text)

# 解析数据
soup = BeautifulSoup(data.text, 'lxml')
# print(soup)

# 提取排行榜数据
video = soup.find('ul', {'class': 'rank-list'})
video = video.find_all('li')

videos = list(video)

ranks = []
coins = []
favorites = []
likes = []
shares = []
video_names = []
play_nums = []
danmu_nums = []
up_names = []
scores = []

# 获取排行榜信息
for rank in videos:
    # 获取视频排名
    video_rank = rank.find('div', {'class', 'num'}).get_text()
    print("视频排名：", video_rank)
    ranks.append(video_rank)

    # 获取视频地址
    video_url = rank.find_all('a')[0].get('href')
    video_url = video_url.replace('//', '')

    # 视频详细数据api
    v_url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid=' + \
            video_url.replace('www.bilibili.com/video/av', '')[:-1]

    # headers里面大小写均可
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    video_data = requests.get(v_url, headers=headers).json()

    # 获取视频详细数据
    details = video_data['data']
    coin = details['coin']
    coins.append(coin)

    favorite = details['favorite']
    favorites.append(favorite)

    like = details['like']
    likes.append(like)

    share = details['share']
    shares.append(share)

    print('硬币数：', coin, ';收藏数：', favorite, ';点赞数：', like, ';转发数：', share)

    print("视频链接：", video_url)

    # 获取视频名称
    video_name = rank.find('div', {'class': 'lazy-img cover'})
    video_name = video_name.find('img').get('alt')
    video_names.append(video_name)
    print("视频名称：", video_name)

    # 获取播放量
    play_num = details['view']
    play_nums.append(play_num)
    print("播放量：", play_num)

    # 获取弹幕数量
    danmu_num = details['danmaku']
    danmu_nums.append(danmu_num)
    print("弹幕数：", danmu_num)

    # 获取UP主名称
    up_name = rank.find_all('span', {'class': 'data-box'})[2].get_text()
    up_names.append(up_name)
    print("UP主ID：", up_name)

    # 获取综合得分
    score = rank.find('div', {'class': 'pts'}).get_text()
    score = score.replace('综合得分', '').replace('\n', '')
    scores.append(score)
    print("综合得分：", score)

    print("")

print("排名：", ranks)
print("视频名称：", video_names)
print("UP主名称：", up_names)
print("点赞数：", likes)
print("硬币数：", coins)
print("收藏数：", favorites)
print("转发数：", shares)
print("播放量：", play_nums)
print("弹幕数：", danmu_nums)
print("综合评分：", scores)

nums = len(ranks)

# 设置列名
worksheet.write(0, 0, '排名')
worksheet.write(0, 1, '视频名称')
worksheet.write(0, 2, 'UP主名称')
worksheet.write(0, 3, '点赞数')
worksheet.write(0, 4, '硬币数')
worksheet.write(0, 5, '收藏数')
worksheet.write(0, 6, '转发数')
worksheet.write(0, 7, '播放量')
worksheet.write(0, 8, '弹幕数')
worksheet.write(0, 9, '综合评分')

# 设置各列宽度
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 20)
worksheet.set_column('E:E', 20)
worksheet.set_column('F:F', 20)
worksheet.set_column('G:G', 20)
worksheet.set_column('H:H', 20)
worksheet.set_column('I:I', 20)
worksheet.set_column('J:J', 20)

# 循环将各项数据放入对应的列
for i in range(1, nums+1):
    worksheet.write(i, 0, ranks[i-1])
    worksheet.write(i, 1, video_names[i-1])
    worksheet.write(i, 2, up_names[i-1])
    worksheet.write(i, 3, likes[i-1])
    worksheet.write(i, 4, coins[i-1])
    worksheet.write(i, 5, favorites[i-1])
    worksheet.write(i, 6, shares[i-1])
    worksheet.write(i, 7, play_nums[i-1])
    worksheet.write(i, 8, danmu_nums[i-1])
    worksheet.write(i, 9, scores[i-1])

workbook.close()