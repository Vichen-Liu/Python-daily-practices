import re
import pandas as pd
with open("D:\\学习\\Python 100题\\Introduction of Jay Chou",encoding="utf-8")as f:
    content=f.read()
words=re.split("[\\s?!\.;,()/]+",content)
word_series=pd.Series(words)
print(word_series.value_counts()[:20])

