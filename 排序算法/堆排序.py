#堆通常用以为数组来实现。在阵列起始位置为0情况下，
#父亲节点i的左子节点位置为2*i+1
#父亲节点i的右子节点位置为2*i+2
#子节点i的父节点位置为floor（（i-）/2））

def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点

    left=2*root+1
    right=left+1
    larger=root
    if (left<HeapSize and heap[larger]<heap[left]):
        larger=left
    if (right<HeapSize and heap[larger]<heap[right]):
        larger=right
    if larger!=root:
        heap[larger],heap[root]=heap[root],heap[larger]
        MAX_Heapify(heap,HeapSize,larger)
    #print (heap)  

def Build_MAX_Heap(heap):

    HeapSize=len(heap)
    for i in range((HeapSize-2)//2,-1,-1):
        MAX_Heapify(heap,HeapSize,i)
    print (heap)


def Heap_Sort(heap):

    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i]=heap[i],heap[0]
        MAX_Heapify(heap,i,0)
    return heap


if __name__=='__main__':
    a=[30,50,57,77,62,78,94,80,84]
    print (a)
    Heap_Sort(a)
    print (a)
