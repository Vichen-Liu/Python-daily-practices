import jieba.posseg as pseg
import re
from collections import Counter
text="""
郭靖与黄蓉并肩而行，心中想着洪七公传授的武功。
欧阳锋忽然现身，冷笑一声。
黄蓉低声道：“靖哥哥，小心欧阳锋。”
郭靖点头，目光坚定。
洪七公在一旁哈哈大笑，说道：“好徒儿，今日便再教你一招。”
"""
words=pseg.cut(text)
jieba_names=[word for word,flag in words if flag=='nr']
surnames=("欧阳|慕容|皇甫|上官|"
    "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨"
    "朱秦尤许何吕施张孔曹严华金魏陶姜")
pattern=re.compile(rf'(?:{surnames})[一-龥]{1,2}')
re_names=pattern.findall(text)
all_names=jieba_names+re_names
cleaned_names=[]
for name in all_names:
    if re.fullmatch(r'[一-龥]{2,4}',name):
        cleaned_names.append(name)

name_counter=Counter(cleaned_names)

print("文本中出现的人名及频率：")
for name,freq in name_counter.most_common():
    print(f"{name}:{freq}")