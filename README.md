## 介绍
使用python来剪辑视频！

借助moviepy这个库

github repo: 

[https://github.com/chunleili/cut_video](https://github.com/chunleili/cut_video)

## 安装
你可以使用
```
pip install cut_video
```
来下载。（推荐，因为还会在你系统内安装同名的命令行工具）


或者直接clone这个repo

## 用法
在当前文件夹下

1. 你需要提供mp4视频: full.mp4

2. 你需要在to_erase.json中输入需要剪辑去掉的部分

例如
```json
[   ["0:22", "1:14"],
    ["1:25", "1:30"],
    ["2:13", "2:25"]
]
```

代表我想要去掉0:22-1:14, 1:25-1:30 和2:13-2:25 这三个时间片段, 保留剩下的。

结果在 final.mp4当中

假如你使用pip的方式安装，只需要运行
```
cut_video
```
即可

## 其他运行方式
你还可以运行python脚本的方式来运行

```
python cut_video.py
```

或者如果你安装了jupyter，也可以运行ipython脚本

```
cut_video.ipynb
```

## 视频教程

请见视频教程

https://www.bilibili.com/video/BV1xG4y137WJ/
