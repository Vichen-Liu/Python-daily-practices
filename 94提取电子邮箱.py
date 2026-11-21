import re

content="""
寻隐者12345@qq.com不遇
朝代：唐asdf12dsa#abc.com代
作python666@163.cn者：贾岛
松下问童子，言师python-abc@163.com采药去。
只在python_ant-666@sina,net此山中,云深不知处。
"""
pattern=re.compile(r"""
[0-9a-zA-Z_-]+
@
[0-9a-zA-Z]+
\.
[a-z]{2,4}
""",re.VERBOSE)
results=pattern.findall(content)
for result in results:
    print(result)