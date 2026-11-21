class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("金额必须是整数！")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
        else:
            print("取款失败！")

    def get_balance(self):
        return self.balance

account=BankAccount("Vichen",100)
print(f"当前余额：{account.get_balance()}")
account.deposit(100)
print(f"当前余额：{account.get_balance()}")
account.withdraw(50)
print(f"当前余额：{account.get_balance()}")