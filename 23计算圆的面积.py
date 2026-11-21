import math
r=int(input("圆的半径:"))
def area_of_circle(r):
    area=math.pi*r*r
    area=round(area,2)
    return area
print(area_of_circle(r))