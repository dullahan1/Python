class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, des = ""):
            self.ledger.append({"amount": amount, "description": des})
            self.balance += amount
    
    def withdraw(self, amount, des = ""):
        if amount > 0:
            self.ledger.append({"amount": amount, "description": des})
            self.balance -= amount 
            print("True")
        else:   
            return False
    
    def transfer(self, amount, category_instance):
        if self.withdraw(amount, "Transfer to {}".format(category_instance.description)):
            category_instance.deposit(amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return True
        else:
            return False

    def get_balance(self):
        print(self.balance)

food = Category("Food")
food.deposit(1000, "Initial Balance")
food.withdraw(500,"First Week")
food.withdraw(200,"Second Week")
food.get_balance()




