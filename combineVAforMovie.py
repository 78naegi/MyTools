# 用来将所给路径的子文件夹下的音视频进行合成的脚本，用于电影
# 使用FFmpeg的命令行进行合成，需要将FFmpeg所在路径加入到系统路径中
import os
# 指定路径
path='E:\Movie'
dirs=os.listdir(path)
# print(dirs)
# 对路径中每一个子文件夹
for dir in dirs:
    dirpath=os.path.join(path,dir)
    files=os.listdir(dirpath)
    filepaths=[] # 用来存放要操作的文件的完整文件路径
    for file in files:
        filepaths.append(os.path.join(dirpath,file))
    print(filepaths)
    # .\ffmpeg.exe -i video.m4s -i audio.m4s -i zimu.srt -c copy takt.mkv

    commend='ffmpeg.exe' # 要执行的命令的字符串

    # 将每个文件作为输入添加到字符串中
    for i in filepaths:
        commend=commend+' -i '+ i
    commend =commend + " -c copy "+ filepaths[0]+".mp4" # 命令构造完成，以第一个文件的文件名+‘.mp4'作为合成后的新文件名
    print(commend) # 输出命令进行检查
    ret = os.system(commend) # 接收命令的返回值
    if ret != 0: # 若执行失败，则将失败文件写入日志中
        with open(os.path.join(path,"failed.log"), "a+") as log:
            log.write(dir + "\n")
    else: # 成功则将所用的音视频文件删除
        for i in filepaths:
            os.remove(i)
    #os.system(ffmpeg)
print('Succeed!')