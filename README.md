## 介绍
使用python来剪辑视频！

借助moviepy这个库


## 用法
首先安装moviepy
```
pip install moviepy
```

你需要提供的视频名为: full.mp4

然后在clip_to_erase.json中输入需要剪辑去掉的部分

例如
```json
[   ["0:22", "1:14"],
    ["1:25", "1:30"],
    ["2:13", "2:25"]
]
```

代表我想要去掉0:22-1:14, 1:25-1:30 和2:13-2:25 这三个时间片段, 保留剩下的。


最后运行脚本
```
python cut_video.py
```

或者如果你安装了jupyter，也可以运行ipython脚本

```
cut_video.ipynb
```

## 视频教程

请见视频教程
