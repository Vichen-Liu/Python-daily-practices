import os
data_dir="D:\\30284\\desktop\\TXT"
contents=[]
for file in os.listdir(data_dir):
    file_path=f"{data_dir}/{file}"

    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path,encoding="utf-8") as f:
            contents.append(f.read())
final_content="\n".join(contents)

with open("D:\\30284\\desktop\\TXT\\now.txt","w",encoding="utf-8") as f:
    f.write(final_content)