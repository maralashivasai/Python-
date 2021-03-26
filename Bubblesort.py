def Bubblesort(li):
    length=len(li)
    for i in range(length):
        for j in range(0,length-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    print(li)

st=[12,89,90,34,5,67]

Bubblesort(st)          
