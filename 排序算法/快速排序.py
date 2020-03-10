#快速排序

def Quik_Sort(myList,start,end):

    if start>=end:
        return myList
    i,j=start,end
    base=myList[i]
    while i<j:
        while i<j and myList[j]>base:
            j=j-1
        myList[i]=myList[j]
        while i<j and myList[i]<base:
            i=i+1
        myList[j]=myList[i]
    myList[i]=base
    Quik_Sort(myList,start,i-1)
    Quik_Sort(myList,i+1,end)
    return myList


if __name__=='__main__':
    a=[12,25,64,31,85,74,94,32,45,16]
    print(a)
    Quik_Sort(a,0,len(a)-1)
    print (a)
    
