import requests
import threading
from bs4 import BeautifulSoup


def bangumi_rank():
    # 请求数据
    url = 'https://www.bilibili.com/ranking/all/1/1/3/?spm_id_from=333.334.b_72616e6b696e675f646f756761.8'
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

    # 获取排行榜信息
    for rank in videos:
        # 获取视频排名
        video_rank = rank.find('div', {'class', 'num'}).get_text()
        print("视频排名：", video_rank)

        # 获取视频地址
        video_url = rank.find_all('a')[0].get('href')
        video_url = video_url.replace('//', '')

        print("视频链接：", video_url)

        # 获取视频名称
        video_name = rank.find('div', {'class': 'lazy-img cover'})
        video_name = video_name.find('img').get('alt')
        print("视频名称：", video_name)

        # 获取播放量
        play_num = rank.find_all('span')[0].get_text()
        print("播放量：", play_num)

        # 获取弹幕数量
        danmu_num = rank.find_all('span')[1].get_text()
        print("弹幕数：", danmu_num)

        # 获取UP主名称
        up_name = rank.find_all('span', {'class': 'data-box'})[2].get_text()
        print("UP主ID：", up_name)

        # 获取综合得分
        score = rank.find('div', {'class': 'pts'}).get_text()
        score = score.replace('综合得分', '分')
        print("综合得分：", score)

        print("")

        # 每隔3分钟执行一次
        timer = threading.Timer(180, bangumi_rank)
        timer.start()

def dance_rank():
    # 请求数据
    url = 'https://www.bilibili.com/ranking/all/129/1/3/?spm_id_from=333.334.b_72616e6b696e675f64616e6365.8'
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

    # 获取排行榜信息
    for rank in videos:
        # 获取视频排名
        video_rank = rank.find('div', {'class', 'num'}).get_text()
        print("视频排名：", video_rank)

        # 获取视频地址
        video_url = rank.find_all('a')[0].get('href')
        video_url = video_url.replace('//', '')
        print("视频链接：", video_url)

        # 获取视频名称
        video_name = rank.find('div', {'class': 'lazy-img cover'})
        video_name = video_name.find('img').get('alt')
        print("视频名称：", video_name)

        # 获取播放量
        play_num = rank.find_all('span')[0].get_text()
        print("播放量：", play_num)

        # 获取弹幕数量
        danmu_num = rank.find_all('span')[1].get_text()
        print("弹幕数：", danmu_num)

        # 获取UP主名称
        up_name = rank.find_all('span', {'class': 'data-box'})[2].get_text()
        print("UP主ID：", up_name)

        # 获取综合得分
        score = rank.find('div', {'class': 'pts'}).get_text()
        score = score.replace('综合得分', '分')
        print("综合得分：", score)

        print("")

        # 每隔3分钟执行一次
        timer = threading.Timer(180, bangumi_rank)
        timer.start()

if __name__=="__main__":
    bangumi_rank()
    print("-------------------------------------------------------------")
    dance_rank()