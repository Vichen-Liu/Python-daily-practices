import random
import string
n=int(input("请输入要生成验证码的位数:"))
characters=string.ascii_letters+string.digits
verify_number=''
for i in range(n):
    verify_number+=random.choice(characters)
print("验证码是:",verify_number)