class Atm :
    def __init__(self,name,amount,pin):
        self.name = name
        self.amount = amount
        self.pin = pin

    def depositMoney(self,amounttobeadded):
        self.amount = self.amount + amounttobeadded
        print("Your New Balance is",self.amount)
    
    def withdrawMoney(self,amounttobededucted):
        if (self.amount>amounttobededucted):
            self.amount = self.amount - amounttobededucted
            print("Your New Balance is",self.amount)
        else : 
            print("Insufficient Balance")
    
    def changePin(self,changedpin):
        oldpin = int(input("Enter Your Old Pin "))
        if (oldpin == self.pin):
            self.pin = changedpin
            print("Your New Pin is",self.pin)
        else :
            print("Incorrect Pin")

customer1 = Atm("Vansh",20000,2345)

customer1.depositMoney(2000)
customer1.withdrawMoney(4000)
customer1.changePin(3456)
        

    
    
