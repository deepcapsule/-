lists=[1,2,3,4,5,6,7,8,9,10]
element=3
def ord_search(lists,element):
    for i in range(0,len(lists)):
        if lists[i]==element:
            print ('lists[{0}]={1}'.format(i,element))
            return i
    else:
         print ('not found')


def bin_search(lists,element):
    low=0
    high=len(lists)-1
    while low<=high:
        mid=(low+high)//2
        if element==lists[mid]:
            print ('lists[{0}]={1}'.format(mid,element))
            return mid
        elif element<lists[mid]:
            high=mid-1
        else:
            low=mid+1
    print('not found')
    return None
i=bin_search(lists,element)
j=ord_search(lists,element)
