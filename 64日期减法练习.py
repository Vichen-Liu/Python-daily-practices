import datetime
def calculate_previous_date(pdate,days):
    pdate_obj=datetime.datetime.strptime(pdate,"%Y-%m-%d")
    print(pdate_obj)
    time_gap=datetime.timedelta(days=days)
    print(time_gap)
    pdate_result=pdate_obj-time_gap
    return pdate_result

print(calculate_previous_date("2025-05-20",1))