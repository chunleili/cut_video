# %%
from moviepy.editor import * 
import json

# %%
# 设定要去掉的时间片段
input_file = "clip_to_erase.json"
erase = None
with open(input_file, "r") as f:
    erase = json.load(f)
print("Erase these clips: ", erase)

# %%
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
full = VideoFileClip("full.mp4")
# 转换为要保留的时间片段
keep = erase_to_keep(full, erase)     
print("Clips to keep:", keep)  
    

# %%
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
final.write_videofile("final.mp4")
