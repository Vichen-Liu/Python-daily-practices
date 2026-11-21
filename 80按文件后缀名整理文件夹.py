import os
import shutil
dir="D:\\30284\\desktop\\刘品涵\\日常"
for file in os.listdir(dir):
    ext=os.path.splitext(file)[1]
    ext=ext[1:]
    print(ext)

    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    sourse_path=f"{dir}/{file}"
    target_path=f"{dir}/{ext}/{file}"
    shutil.move(sourse_path,target_path)
