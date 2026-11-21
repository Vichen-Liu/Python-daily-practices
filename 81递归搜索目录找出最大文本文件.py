import os
search_dir=r"D:\30284\desktop\刘品涵\日常\doc"
result_file=[]
for root,dirs,files in os.walk(search_dir):
    for file in files:
        if file.endswith(".doc"):
            file_path=f"{root}/{file}"
            file_size_kb=os.path.getsize(file_path)/1024
            result_file.append((file_path,file_size_kb))
max_file=max(result_file)
print(f"最大的文本是：",max_file)