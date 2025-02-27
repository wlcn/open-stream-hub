import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import os

base_url = 'https://www.22a5.com'
base_path = 'F:\\music'
# 用户输入的关键字
keyword = input("请输入要搜索的歌曲关键字: ")

print(f"关键字: {keyword}")

def get_song(id):
    # 请求数据
    data = {
        'id': id,
        'type': 'music'
    }
    # 发送 POST 请求
    response = requests.post('https://www.22a5.com/js/play.php', data=data)

    res = response.json()

    title = res['title']
    url = res['url']
    # 输出响应内容
    print(f"歌曲下载详情, name:{title}, url:{url}")

    file_extension = os.path.splitext(url)[1]

    song_response = requests.get(url)

    # 拼接完整路径
    file_path = os.path.join(base_path, keyword, f"{title}{file_extension}")

    # 检查文件夹是否存在，如果不存在则创建
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb') as f:
        f.write(song_response.content)

    print(f"已下载歌曲: {file_path}")

    # 下载歌词
    lrc_response = requests.get(
        f"{base_url}/plug/down.php?ac=music&lk=lrc&id={id}")
    # 拼接完整路径
    lrc_file_path = os.path.join(base_path, keyword, f"{title}.lrc")
    with open(lrc_file_path, 'wb') as f:
        f.write(lrc_response.content)
    print(f"已下载歌词: {lrc_file_path}")


def get_song_detail(url):
    """
    解析指定页面的歌曲下载地址
    :param url: 歌曲页面的 URL
    :return: 歌曲的下载地址
    """
    try:
        detail_url = f"{base_url}{url}"
        print("请求detail地址:", detail_url)
        # 发送 HTTP 请求
        response = requests.get(detail_url)
        response.raise_for_status()  # 检查请求是否成功

        # print("请求的response\n", response.text)
        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        div_tag = soup.find('div', class_='dance_wl')

        # 提取 src 属性
        if div_tag:
            lrc_a_tag = div_tag.find('a', class_='layui-btn lklv')
            txt_a_tag = div_tag.find('a', class_='layui-btn lklan')
            lrc_href = lrc_a_tag['href']
            txt_href = txt_a_tag['href']
            print("音频歌词地址:", lrc_href, txt_href)

            # 解析 URL 中的查询参数
            parsed_url = urlparse(lrc_href)
            query_params = parse_qs(parsed_url.query)

            # 提取 id 参数
            if 'id' in query_params:
                id_value = query_params['id'][0]  # 获取第一个 id 值
                print("解析出的id:", id_value)
                get_song(id_value)
            else:
                print("未找到 id 参数")
        else:
            print("未找到音频文件地址")
    except Exception as e:
        return f"解析失败: {e}"

def get_page(page):
    # 目标URL
    url = f"{base_url}/so/{keyword}/{page}.html"

    print(f"搜索地址: {url}")

    # 发送HTTP请求
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假设歌曲列表在某个特定的HTML标签中
    songs = soup.find('div', class_='play_list').find(
        'ul').find_all('li')  # 根据实际HTML结构调整


    # 搜索歌曲
    for song in songs:
        a_tag = song.find('div', class_='name').find('a')
        title = a_tag.text
        detail_link = a_tag['href']
        print(f"找到歌曲: {title} {detail_link}")
        # 获取下载链接
        get_song_detail(detail_link)

# 第一页数据
for i in range(1, 2):
    get_page(i)



