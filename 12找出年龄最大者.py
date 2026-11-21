people={"张三":18,"李四":50,"王五":29,"赵六":22}
max_age=float('-inf')
max_name=" "
for name,age in people.items():
    if age>max_age:
        max_age=age
        max_name=name
print(max_name,max_age)
