import os
path=r"D:\MyTools\pak"
files=os.listdir(path)
for file in files:
    sub=file[3:]
    # index=file.find('.')
    newname=sub
    os.rename(os.path.join(path, file), os.path.join(path, newname))
    print(file + "is OK!")
    # newname=file[0:index]+'mp4'
    # os.rename(os.path.join(path,file),os.path.join(path,newname))
    # print(file+"is OK!")
