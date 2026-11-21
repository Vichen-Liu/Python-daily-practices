def verify_age(age):
    if age<0 or age>120:
        raise Exception("年龄超出范围！")
    return age
try:
    print(verify_age(190) )
except Exception as e:
    print(e)
print(verify_age(34) )