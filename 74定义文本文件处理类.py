class TextFileHandler:
    def __init__(self,file_path):
        self.file_path=file_path

    def read_file(self):
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                content=f.read()
        except FileNotFoundError:
            return "文件不存在！"
        else:
            return content

    def write_file(self,content):
        with open(self.file_path,"a",encoding="utf-8") as f:
            f.write(content+"\n")

handler=TextFileHandler("D:\\30284\\desktop\\AI.txt")
handler.write_file("Hello!")
print(handler.read_file())