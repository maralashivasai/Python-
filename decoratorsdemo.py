class Cricketer:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    @property    
    def name(self):
        print("get called")
        return self.__name
    @name.setter    
    def name(self,nam):
        print("set called")
        self.__name=nam
    
    @name.deleter
    def name(self):
        print("del called")
        del self.__name
    @property    
    def age(self):
        print("get called")
        return self.__age
    @age.setter    
    def age(self,ag):
        print("set called")
        self.__age=ag
    
    @name.deleter
    def age(self):
        print("del called")
        del self.__age

c1=Cricketer('Joe',27)
c1.name="Steve"
print(c1.name)
del c1.name
#print(c1.name)

c1.age=67
print(c1.age)
del c1.age
print(c1.age)
