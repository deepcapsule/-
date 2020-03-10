#归并排序

def merge(a,b):

    c=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
    if i==len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c


def merge_Sort(lists):
    if len(lists)<=1:
        return lists
    middle=len(lists)//2
    left=merge_Sort(lists[:middle])
    right=merge_Sort(lists[middle:])
    return merge(left,right)
    


if __name__=='__main__':
    a=[12,45,62,32,75,94,52,14,61,24]
    print (a)
    print (merge_Sort(a))
   
