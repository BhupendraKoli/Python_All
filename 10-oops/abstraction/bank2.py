from bank1 import bank

class imp (bank):
     def __init__(self,holdername,blance):
        self.holdername=holdername
        self.blance=blance
     def disp(self):
         print(f"the account holder name is {self.holdername} and tha blance of the acount is {self.blance}")
     def deop(self,amount):
        self.blance=self.blance+amount
        print(f" the diposited amount is {amount} the total is {self.blance}")
     def withd(self,amount1):
        if amount1 > self.blance:
            print("insifecient blance ")
        else:
            self.blance=self.blance-amount1
            print(f"the withrdro amount is {amount1} tatal ramaing balnce {self.blance}")       
     