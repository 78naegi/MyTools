# 用来将所给路径的子文件夹下的音视频进行合成的脚本，用于电视剧
# 使用FFmpeg的命令行进行合成，需要将FFmpeg所在路径加入到系统路径中
import os
# 指定路径
path='E:\Drama'
dirs=os.listdir(path)
# print(dirs)
# 对路径中每一个子文件夹
for dir in dirs:
    dirpath=os.path.join(path,dir)
    files=os.listdir(dirpath)
    # 要求音视频文件名前缀相同，确保能排列在一起
    for j in range(0,len(files),2):
        filepaths = []  # 用来存放要操作的文件的完整文件路径
        commend = 'ffmpeg.exe'  # 要执行的命令的字符串
        videoname=os.path.join(dirpath,str(int(j/2+1))) # 集数不准确，需要之后手动命名
        filepaths.append(os.path.join(dirpath,files[j]))
        filepaths.append(os.path.join(dirpath,files[j+1]))
        print(filepaths)
        commend = commend + ' -i ' + filepaths[0]+' -i '+ filepaths[1]+ " -c copy "+ videoname+".mp4"
        print(commend) # 输出命令进行检查
        ret = os.system(commend)  # 接收命令的返回值
        if ret != 0:  # 若执行失败，则将失败文件写入日志中
            with open(os.path.join(path, "failed.log"), "a+") as log:
                log.write(dir + "\n")
        else:  # 成功则将所用的音视频文件删除
            for i in filepaths:
                os.remove(i)

    #os.system(ffmpeg)
print('Done!')