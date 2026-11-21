import re
import jieba
content="""
路灯把影子拉得很长,
像一封寄不出的信.
风经过的时候,
我听见远方在翻页.
而此刻,
月光正替我,
把沉默折成纸船,
放逐在,
无人经过的河面.
"""
print(re.sub(r"[\\s,.]","",content))
word_list=jieba.cut(content)
print(word_list)