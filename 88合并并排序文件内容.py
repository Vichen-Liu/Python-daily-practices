def read_file(file_path):
    with open(file_path,encoding="utf-8")as f:
        content=f.read()
    return content
content1=read_file("D:\\学习\\Python 100题\\test1")
content2=read_file("D:\\学习\\Python 100题\\test2")
combined_content=content1+content2
sorted_content="".join(sorted(combined_content))
with open("test.3","w",encoding="utf-8")as f:
    f.write(sorted_content)
