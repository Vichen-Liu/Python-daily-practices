class Calculator:
    def add(self,a,b):
        return a+b

    def subtrack(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b==0:
            raise ValueError("除数不能为0！")
        return a/b

calculator=Calculator()
print(calculator.add(2,9))
print(calculator.subtrack(2,9))
print(calculator.multiply(2,9))
print(calculator.divide(2,9))