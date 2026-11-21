import datetime
birth_day="2007-5-7"
birth=datetime.datetime.strptime(birth_day,"%Y-%m-%d")
current_datetime=datetime.datetime.now()
minus_datetime=current_datetime-birth
print(minus_datetime.days)