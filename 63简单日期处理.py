import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d"))
birthday=datetime.date(1941,1,5)
print("宫崎骏生日：",birthday)
birth_next_day=birthday+datetime.timedelta(days=1)
print("宫崎骏生日的下一天：",birth_next_day)
first_birthday=birthday.replace(year=birthday.year+1)
print("宫崎骏的一岁生日是：",first_birthday)