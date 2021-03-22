import csv

file=open('D:\python/record.csv','r')
with file:
    read=csv.DictReader(file)
    for row in read:
        print(dict(row))


name=['Firstname', 'lastname'
      'Shivasai' ,  'Marala'
      'shivateja',  'Marala']
file=open('D:\python/recorddup.csv','w')
file.seek(0)
with file:
    fwr=csv.writer(file)
    for row in name:
        fwr.writerow(row)
file.close()


file=open('D:\python/recorddup2.csv','w')
with file:
    fnames=['Firstname','lastname']
    wr=csv.DictWriter(file,fieldnames=fnames)
    wr=Writeheader()
    wr=Writerow({'Firstname':'shiva' ,'lastname':'sai' })
    wr=Writerow({'Firstname':'shiva' ,'lastname':'sai' })  

