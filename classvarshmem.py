class Comp:
    participants=[]
    def __init__(self,name,price):
        self.name=name
        self.price=price

debate=Comp("Debate",500)
print(debate.name,debate.price)

Comp.participants.append("shiva")
essay=Comp("Essay",600)
essay.participants.append("sai")

print(Comp.participants)
