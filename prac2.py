file=open("file.txt",'r')
d={}
for line in file:
    (a,b)=line.strip().split(',')
    d[a]=int(b)
print(d)
