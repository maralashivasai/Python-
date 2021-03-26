
def Selectionsort(li):
   
    
    
    length=len(li)
    print(length)
    for i in range(length):
        minindex=i
        for j in range(i+1,length):
            if li[minindex]>li[j]:
                minindex=j
                print(li[minindex])
                
        (li[i],li[minindex])=(li[minindex],li[i])
        print(li)
    #print(li)

st=[20,12,10,15,2]

Selectionsort(st)
