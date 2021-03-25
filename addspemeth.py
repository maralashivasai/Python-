class Saving:
    def __init__(self,amount):
        self.__amount=amount
    def __add__(self,ot):
        return self.__amount+ot.__amount
    
s1=Saving(100)
s2=Saving(500)

print(s1+s2)
