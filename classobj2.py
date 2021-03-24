class Hello:
    def __init__(self,name):
        self.name=name
        self.email=name+'.'+"@xyz.com"
        
s1=Hello(input())
print(s1.name,s1.email)
s1.name="sai"
print(s1.name,s1.email)
