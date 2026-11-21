import re
def verify_password(password):
    if not 6<=len(password)<=20:
        return False,"密码必须在6-20之间"
    if not re.findall(r"[a-z]",password):
        return False,"密码必须包含至少1个小写字母"
    if not re.findall(r"[A-Z]",password):
        return False,"密码必须包含至少1个大写字母"
    if not re.findall(r"\d",password):
        return False,"密码必须包含至少1个数字"
    if not re.findall(r"\W",password):
        return False,"密码必须包含至少1个特殊字符"
    return True,None

print("Helloworld#666",verify_password("Helloworld#666"))
print("lph20070507",verify_password("lph20070507"))