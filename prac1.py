import csv
dix={}
li=[]
file=open("D:\python/record1.csv",'r')
with file:
    data=csv.DictReader(file)
    print(data)
    for row in data:
        li.append(dict(row))
print(li)
print()
dix=dict(li)

print(dix)


