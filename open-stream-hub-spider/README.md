# Downloand music

## Download by keyword

```shell
python www.22a5.com.py
```

output log

```log
PS E:\long.wang\vscode\music> python .\www.22a5.com.py
请输入要搜索的歌曲关键字: 伍佰
关键字: 伍佰
搜索地址: https://www.22a5.com/so/伍佰/1.html
找到歌曲: 伍佰 & China Blue《再度重相逢》 /mp3/klexmmcl.html
请求detail地址: https://www.22a5.com/mp3/klexmmcl.html
音频歌词地址: /plug/down.php?ac=music&lk=lrc&id=klexmmcl /plug/down.php?ac=music&lk=txt&id=klexmmcl
解析出的id: klexmmcl
歌曲下载详情, name:伍佰 & China Blue《再度重相逢》[Mp3_Lrc], url:https://lu-sycdn.kuwo.cn/fec68d3e289b42be4ce6bd030f438c92/67b08a22/resource/a3/86/84/1662373353.aac
已下载歌曲: F:\music\伍佰\伍佰 & China Blue《再度重相逢》[Mp3_Lrc].aac
已下载歌词: F:\music\伍佰\伍佰 & China Blue《再度重相逢》[Mp3_Lrc].lrc
```

## Download by ID

```shell
python www.22a5.com.detail.py
```

output log

```log
PS E:\long.wang\vscode\music> python www.22a5.com.detail.py
关键字: 单曲
请输入歌曲ID: easkkdxls
歌曲下载详情, name:陈奕迅《孤勇者》[Mp3_Lrc], url:https://lv-sycdn.kuwo.cn/a50d0810cb6c12906ba7653c861590d7/67c003a1/resource/30106/trackmedia/M500001hE0cD4NPYfX.mp3
已下载歌曲: F:\music\单曲\陈奕迅《孤勇者》[Mp3_Lrc].mp3
已下载歌词: F:\music\单曲\陈奕迅《孤勇者》[Mp3_Lrc].lrc
```