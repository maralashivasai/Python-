class Comp:
    __rp=1.4
    def __init__(self,name,pr):
        self.__name=name
        self.__pr=pr
    def getname(self):
        return self.__name
    def setname(self,nam):
        self.__name=nam
    def getpr(self):
        return self.__pr
    def setpr(self,prr):
        self.__pr=prr
    def rpp(self):
        self.__pr*=self.__rp
    @classmethod
    def getrp(cls):
        return cls.__rp
    @classmethod
    def setrp(cls,r):
        cls.__rp=r
    @classmethod
    def sstr(cls,co):
        nam,val=co.split('-')
        return cls(nam,val)

c1=Comp("swim",100)
print(c1.getname())
print(c1.getpr())
c1.rpp()
print(c1.getpr())


st="Cricket-5000"
print(Comp.sstr("heoo-89"))
c2=Comp.sstr(st)



print(c2.getname())
print(c2.getpr())

        
    
    
        
