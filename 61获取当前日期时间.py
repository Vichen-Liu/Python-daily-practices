import datetime
current_datetime=datetime.datetime.now()
print(current_datetime)
time_str=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(time_str)
print(current_datetime.year)