import datetime
def get_date_range(begin_date_object,end_date_object):
    begin_date_object=datetime.datetime.strptime(begin_date_object,"%Y-%m-%d")
    end_date_object = datetime.datetime.strptime(end_date_object, "%Y-%m-%d")
    date_list=[]
    current_date=begin_date_object
    while current_date<=end_date_object:
        current_time_str=current_date.strftime("%Y-%m-%d")
        date_list.append(current_time_str)
        current_date+=datetime.timedelta(days=1)
    return date_list
begin_date="2025-05-20"
end_date="2025-06-01"
print(get_date_range(begin_date,end_date))