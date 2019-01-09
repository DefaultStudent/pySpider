import requests
from bs4 import BeautifulSoup

# 请求数据
url = 'https://www.bilibili.com/ranking/all/1/1/3'
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
    play_num = rank.find_all('span')[0].get_text()
    play_nums.append(play_num)
    print("播放量：", play_num)

    # 获取弹幕数量
    danmu_num = rank.find_all('span')[1].get_text()
    danmu_nums.append(danmu_num)
    print("弹幕数：", danmu_num)

    # 获取UP主名称
    up_name = rank.find_all('span', {'class': 'data-box'})[2].get_text()
    up_names.append(up_name)
    print("UP主ID：", up_name)

    # 获取综合得分
    score = rank.find('div', {'class': 'pts'}).get_text()
    score = score.replace('综合得分', '分').replace('\n', '')
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