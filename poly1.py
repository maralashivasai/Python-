class Bankacc:
    def __init__(self,bal):
        self.__bal=bal
    def withdraw(self,val):
        self.__bal-=val
        print("amoun drawn",val)
        print("balance",self.__bal)
    def deposit(self,val):
        self.__bal+=val
        print("balalnce",self.__bal)


class currentacc(Bankacc):
    def __init__(self,bala):
        super().__init__(bala)
    def withdraw(self,va):
        if va >100:
            print("contact bank")
        else:
            super().withdraw(va)

c=currentacc(1500)
c.withdraw(67)
c.deposit(100)
