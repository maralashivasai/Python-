class student:
    def __init__(self,name,gpa):
        self.__name=name
        self.__gpa=gpa
        self.__club=set()

    def setname(self,name):
        self.__name=name
    def setgpa(self,gpa):
        self.__gpa=gpa
    def addcu(self,club):
        self.__club.add(club)

    def printdata(self):
        print(self.__name,
        self.__gpa,
        self.__club)

s=student("shiva",9.5)
s.setname(input("Enter name"))
s.setgpa(float(input("Enter gpa")))
s.addcu(input("neter club"))

s.printdata()
studo=[{'name':"s",'gpa':4.9,'club':['chess','holkey']},
      {'name':"shkh",'gpa':4.0,'club':['chesjbs','holhvkey']}
      ]
def Stde(stud):
    stli=[]
    for stde in stud:
        if 'name' not in stde and 'gpa' in stde:
            continue
        s=student(stde['name'],stde['gpa'])
        if 'club' in stde:
            for i in stde['club']:
                s.addcu(i)

    stli.append(s)
st=Stde(studo)

print(st)


    



    
