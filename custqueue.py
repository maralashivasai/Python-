class Myqueue:
    def __init__(self):
        self.li=[]
    def enqueue(self,item):
        self.li.append(item)
    def dequeue(self):
        self.li.pop(0)
    def isempty(self):
        return len(self.li)==0
    def printdata(self):
        print(self.li)
q=Myqueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.printdata()

        
