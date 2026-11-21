import re
content="""
小明上街买菜
买了1斤黄瓜花了8元；
买了2斤葡萄花了13.5元；
买了3斤白菜花了5.4元；
"""
for line in content.split("\n"):
    pattern=r"(\d)斤(.+)花了(\d+(\.\d+)?)元"
    match=re.search(pattern,line)

    if match:
        print(f"{match.groups()[0]}\t{match.groups()[1]}\t{match.groups()[2]}")
