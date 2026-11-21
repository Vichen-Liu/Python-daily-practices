class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def describe(self):
        return f"品牌：{self.make},型号：{self.model}"

class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year=year
    def describe(self):
        return f"品牌：{self.make},型号：{self.model},年份：{self.year}"

car=Car("Toyota","Camry",2025)
print(car.describe())