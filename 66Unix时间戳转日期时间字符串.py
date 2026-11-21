import datetime
unix_time=1620747224
datetime_object=datetime.datetime.fromtimestamp(unix_time)
print(datetime_object)
date_str=datetime_object.strftime("%Y/%m/%d %H:%M:%S")
print(date_str)