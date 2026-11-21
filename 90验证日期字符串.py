import re

def date_is_right(data):
    return re.match(r"\d{4}-\d{2}-\d{2}",data) is not None

date1="2025-02-07"
date2="202-05-20"
date3="2021/05-20"
date4="20210520"
date5="202a-05-20"

print(date1,date_is_right(date1))
print(date2,date_is_right(date2))
print(date3,date_is_right(date3))
print(date4,date_is_right(date4))
print(date5,date_is_right(date5))

"""
正则表达式
"""