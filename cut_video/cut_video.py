from moviepy.editor import * 
import json
import argparse
import sys
import os
print("Importing cut_video.py")

'''
简单地剪辑视频文件！

请在当前目录下创建一个json文件，文件名为to_erase.json，内容为要去掉的时间片段，例如：
[   ["0:22", "1:14"],
    ["1:25", "1:30"],
    ["2:13", "2:25"]
]

然后准备一个视频文件，例如full.mp4，运行：
```python
python cut_video.py
```

最后得到的视频文件为final.mp4
'''
def run(input_file='full.mp4', output_file='final.mp4', json_file="to_erase.json"):
    #读取参数
    parser = argparse.ArgumentParser(description="Cut video by moviepy!\n \
        Please create a json file named to_erase.json in the current directory, \
        the content is the time segments to erase, for example:\n \
        [   [\"0:22\", \"1:14\"],\n \
            [\"1:25\", \"1:30\"],\n \
            [\"2:13\", \"2:25\"]\n \
        ]\n \
        Then prepare a video file, for example: full.mp4\n\
    ")
    parser.add_argument("--input", default='full.mp4', help="input video file")
    parser.add_argument("--output", default='final.mp4', help="output video file")
    input_file = parser.parse_args().input
    output_file = parser.parse_args().output

    # 设定要去掉的时间片段
    json_file = "to_erase.json"
    erase = None
    with open(json_file, "r") as f:
        erase = json.load(f)
    print("Erase these clips: ", erase)

    # 将要去掉时间片段转换为要保留的时间片段
    def erase_to_keep(full, erase):
        flat_list = [item for sublist in erase for item in sublist]
        flat_list.insert(0, 0)
        flat_list.append(full.duration)
        keep = []
        for i in range(0, len(flat_list), 2):
            keep.append([flat_list[i], flat_list[i+1]])
        return keep

    # 读取视频文件
    full = VideoFileClip(input_file)
    # 转换为要保留的时间片段
    keep = erase_to_keep(full, erase)     
    print("Clips to keep:", keep)  
        

    # 利用subclip将要保留的时间片段剪切出来
    def keep_some_clip(full, keep):
        clips = []
        for i, cut in enumerate(keep):
            print(f"Cutting clip No.{i}, start {cut[0]}, end {cut[1]}")
            clip = full.subclip(cut[0], cut[1])
            clips.append(clip)
        return clips

    clips = keep_some_clip(full, keep)
    final = concatenate_videoclips(clips)
    final.write_videofile(output_file)

if __name__ == '__main__':
    run()