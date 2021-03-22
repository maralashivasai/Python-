import csv

file=open('D:\python/record.csv','r')
with file:
    read=csv.reader(file)
    for row in read:
        print(row)

file=open('D:\python/recordpipe.csv','r')
with file:
    read=csv.reader(file,delimiter='|')
    for row in read:
        print(row)

        

file=open('D:\python/recordtab.csv','r')
with file:
    read=csv.reader(file,delimiter='\t')
    for row in read:
        print(row)

        

    
