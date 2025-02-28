import os
from pydub import AudioSegment

source = "./music/"  #源文件夹
target = "./output/"  #输出文件夹
source_form = "opus"  #原格式
target_form = "mp3"  #输出格式

files = os.listdir(source)  #返回源文件夹下的所有文件和目录名
for file in files:  #遍历文件
    length = len(source_form)
    if source_form == "flac":
        song = AudioSegment.from_file(source + file)  #读取音频文件
    elif source_form == "mp3":
        song = AudioSegment.from_mp3(source + file)
    elif source_form == "wav":
        song = AudioSegment.from_wav(source + file)
    elif source_form == "ogg":
        song = AudioSegment.from_ogg(source + file)
    elif source_form == "opus":
        song = AudioSegment.from_file(source + file)
    else:
        print("没有这种格式！")
    song.export(target + f"{file[:-length]}" + target_form, format=target_form)  #保存音频为新的格式
    print(f"{file[:-length]}" + target_form)  #输出结果
