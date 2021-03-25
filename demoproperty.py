class Cricketer:
    def __init__(self):
        self.__name=""
    def setname(self,nam):
        print("set called")
        self.__name=nam
    def getname(self):
        print("get called")
        return self.__name
    def delname(self):
        print("del called")
        del self.__name
    name=property(getname,setname,delname)

c1=Cricketer()
c1.name="kane"
print(c1.name)
del c1.name
