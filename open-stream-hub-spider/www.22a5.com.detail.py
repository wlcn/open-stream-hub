import requests
import os

base_url = 'https://www.22a5.com'
base_path = 'F:\\music'
# 用户输入的关键字
keyword = "单曲"

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

song_id = input("请输入歌曲ID: ")
get_song(song_id)



