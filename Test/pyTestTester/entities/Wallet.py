class Wallet(object):
    balance = 0
    pincode = 0
    isOverDrafted = False

    def __init__(self, initialAmout, pinCode):
        self.balance = initialAmout
        self.pincode = pinCode

    def withdraw(self, amount, pincode):
        if self.pincode == pincode and type(amount) == int:
            if (self.balance - amount) >= 0:
                self.balance = self.balance - amount
                print("withdrawing " + str(amount) + " current balance is: " + str(self.balance))
            else:
                raise Exception("insufficent funds")
        else:
            raise Exception("Wrong pincode")

    def addMoney(self, amount):
        if type(amount) == int:
            self.balance = self.balance + amount
            print("Adding " + str(amount) + " current balance is: " + str(self.balance))
        else:
            raise Exception("please enter the number in well... numbers")

    def checkBalance(self, pincode):
        if pincode == self.pincode:
            return self.balance
        else:
            raise Exception("Wrong pincode")
