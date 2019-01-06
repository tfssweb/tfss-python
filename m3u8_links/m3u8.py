import requests
import re
import pymysql.cursors
from bs4 import BeautifulSoup

'''
爬取http://www.mp4sf.com/
'''


def gethtml(play_url,xiangqing_url):
    # 连接MySQL数据库。
    connection = pymysql.connect(host='172.18.18.203', port=23306, user='root', password='root', db='db_mrliu',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    # 通过cursor创建游标
    cursor = connection.cursor()

    # 播放页
    play_html = requests.get(play_url)
    play_html.raise_for_status()

    # 详情页
    xiangqing_html = requests.get(xiangqing_url)
    xiangqing_html.raise_for_status()

    try:
        # 解析 HTML源代码
        soup = BeautifulSoup(play_html.text, 'html.parser')
        xiangqing_soup = BeautifulSoup(xiangqing_html.text, 'html.parser')

        # 获取缩略图
        images = xiangqing_soup.select('img')
        for image in images:
            if image.has_attr('data-original'):
                video_thumbnail = 'http://www.mp4sf.com'+ image['data-original']
                print(image['data-original'])
                print(video_thumbnail)

        # 获取电影名称
        video_name = soup.select('h1')[0].text
        print(video_name)

        # 获取电影URL: m3u8
        video_urls = re.findall(".*\"url\":\"(.*)\"\,\"url_next.*", str(soup))
        video_url = video_urls[0].replace('\\', '')
        print(video_url)

        # 缩略图
        # video_thumbnail = '/static/images/noimg.jpg'
        # 视频格式
        video_pattern = 'video/m3u8'

        # 视频简介
        video_infos = re.compile(r'<span class="detail-content" style="display: none;">(.*)</span>')
        video_info = re.findall(video_infos, str(soup))[0]
        print(video_info)

        # 视频类型
        video_types = re.compile(r'<span class="text-muted">类型：</span>(.*\t)')
        video_type = re.findall(video_types, str(soup))[0]
        print(video_type)

        # 视频地区
        video_areas = re.compile(r'<span class="text-muted">地区：</span>(.*\t)')
        video_area = re.findall(video_areas, str(soup))[0]
        print(video_area)

        # 视频年代
        video_years = re.compile(r'<span class="text-muted">年份：</span>(.*\t)')
        video_year = re.findall(video_years, str(soup))[0]
        print(video_year)

        # 清晰度
        video_claritys = re.compile(r'<span class="pic-text text-right">(.*)</span>')
        video_clarity = re.findall(video_claritys, str(soup))[0]
        print(video_clarity)

        insret_sql = """
            INSERT INTO `t_ckplayer_video`(`video_name`,`video_url`,`video_thumbnail`,`video_pattern`,`video_info`,`video_type`,`video_area`,`video_year`,`video_clarity`) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(insret_sql, (
            video_name, video_url, video_thumbnail, video_pattern, video_info, video_type, video_area, video_year,
            video_clarity))
        connection.commit()
        # 关闭数据连接
        connection.close()

    except Exception as e:
        print(e)


# 删除不符合条件的URL
def delete():
    # 连接MySQL数据库。
    connection = pymysql.connect(host='172.18.18.203', port=23306, user='root', password='root', db='db_mrliu',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    # 通过cursor创建游标
    cursor = connection.cursor()
    delete_sql = "DELETE FROM `t_ckplayer_video` where `video_url` not like 'http%'"
    cursor.execute(delete_sql)

    connection.commit()

    # 关闭数据连接
    connection.close()


# http://www.mp4sf.com/play/28839-1-1.html


BASE_URL = 'http://www.mp4sf.com/'
PLAY_URL = 'play/'
XIANGQING_URL = 'xiangqing/'
PAGE_URL = '2'

for n in range(2):
    play_url = BASE_URL + PLAY_URL + PAGE_URL + str(n) + '-1-1.html'
    xiangqing_url = BASE_URL + XIANGQING_URL + PAGE_URL + str(n) + '.html'

    gethtml(play_url,xiangqing_url)

delete()

print("爬取完毕")